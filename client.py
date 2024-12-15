import grpc
import glossary_pb2
import glossary_pb2_grpc

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = glossary_pb2_grpc.GlossaryServiceStub(channel)
        print("Adding a new term")
        response = stub.AddTerm(glossary_pb2.Term(keyword="SomeKey", description="some_description"))
        print(response.message)
        print("Updating a term")
        response = stub.UpdateTerm(glossary_pb2.Term(keyword="SomeKey", description="some_other_description"))
        print(response.message)
        print("Listing all terms")
        terms = stub.ListTerms(glossary_pb2.Empty())
        for term in terms.terms:
            print(f"{term.keyword}: {term.description}")

if __name__ == "__main__":
    run()
