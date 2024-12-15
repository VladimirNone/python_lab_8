from concurrent import futures
import grpc
import glossary_pb2
import glossary_pb2_grpc
from database import add_term, update_term, delete_term, get_term, list_terms
from schemas import Term, TermRequest
from pydantic import ValidationError

class GlossaryServiceServicer(glossary_pb2_grpc.GlossaryServiceServicer):
    def ListTerms(self, request, context):
        terms = list_terms()
        return glossary_pb2.TermList(terms=[glossary_pb2.Term(**term) for term in terms])

    def GetTerm(self, request, context):
        try:
            data = TermRequest(keyword=request.keyword)
            term = get_term(data.keyword)
            if term:
                return glossary_pb2.Term(**term)
            context.abort(grpc.StatusCode.NOT_FOUND, "Term not found.")
        except ValidationError as e:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, str(e))

    def AddTerm(self, request, context):
        try:
            data = Term(keyword=request.keyword, description=request.description)
            success, message = add_term(data.keyword, data.description)
            return glossary_pb2.OperationStatus(success=success, message=message)
        except ValidationError as e:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, str(e))

    def UpdateTerm(self, request, context):
        try:
            data = Term(keyword=request.keyword, description=request.description)
            update_term(data.keyword, data.description)
            return glossary_pb2.OperationStatus(success=True, message="Term updated successfully.")
        except ValidationError as e:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, str(e))

    def DeleteTerm(self, request, context):
        try:
            data = TermRequest(keyword=request.keyword)
            delete_term(data.keyword)
            return glossary_pb2.OperationStatus(success=True, message="Term deleted successfully.")
        except ValidationError as e:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, str(e))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    glossary_pb2_grpc.add_GlossaryServiceServicer_to_server(GlossaryServiceServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
