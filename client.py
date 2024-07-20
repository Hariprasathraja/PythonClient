import grpc
import bank_pb2
import bank_pb2_grpc

class AccountClient:
    def __init__(self,channel):
        self.stub=bank_pb2_grpc.AccountServiceStub(channel)

    def get_account_details(self,account_number):
        request=bank_pb2.AccountRequest(accountnumber=account_number)
        response=self.stub.GetAccountDetails(request)
        print(f"Account name:{response.name}")
        print(f"Account Balance: {response.balance}")

    def create_account(self,name,initial_balance):
        request=bank_pb2.CreateAccountRequest(name=name,initial_balance=initial_balance)
        response=self.stub.CreateAccount(request)
        print(f"Created Account Number: {response.accountnumber}")
        print(f"Account name: {response.name}")
        print(f"Account Balance: {response.balance}")

def main():
    channel=grpc.insecure_channel('localhost:50051')
    client=AccountClient(channel)

    client.get_account_details(12345)

    client.create_account("Hari",6000.60)

    channel.close()

if __name__=='__main__':
    main()
    