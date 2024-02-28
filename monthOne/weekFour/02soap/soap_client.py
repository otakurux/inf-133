from zeep import Client

client = Client('http://localhost:8000')

result_one = client.service.greet(name="Deivid")
print(result_one)

result_two = client.service.sum(num1=5, num2=3)
print(result_two)

result_three = client.service.is_palindrome(word="deivied")
print(result_three)
