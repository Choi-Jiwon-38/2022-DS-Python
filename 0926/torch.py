from requests import request
import torch
# Tensor <- 스칼라, 벡터, 행렬 등을 일반화한 개념

x1 = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
x2 = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.int)   # type을 지정할 때는 dtype을 이용
x3 = torch.IntTensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])                 # IntTensor, LongTensor 등으로도 type을 지정해주는 방법도 있음
print(x1)
print(x1.type())        # type을 보고 싶을 때
print(x2.type()) 

print(x1.shape)         # [3, 3] <- 3행 3열의 크기
print(x1.size())        # 위 shape과 동일한 기능을 수행 

# dimension을 구하는 방법
print(x1.ndim)          # dimension의 개수 <- 가장 많이 사용
print(x1.ndimension())  # ndim과 동일한 기능
print(len(x1.shape))     # 위 두 가지와 동일한 기능

# tensor의 모양 바꾸기

# unsqueeze(x, i): tensor x에 i번째 차원을 추가
a = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
a0 = torch.unsqueeze(a, 0)
a1 = torch.unsqueeze(a, 1)
a2 = torch.unsqueeze(a, 2)

print("a0: ", a0)
print("a1: ", a1)
print("a2: ", a2)

print("a0.shape: ", a0.shape) # 0칸 안쪽에 [ ] <- 차원 추가
print("a1.shape: ", a1.shape) # 1칸 안쪽에 [ ]
print("a2.shape: ", a2.shape) # 2칸 안쪽에 [ ]

# squeeze: tensor x의 차원을 제거 <- shape을 하였을 때 1을 값는 차원 (불필요한 차원) 제거 용도
print(a2)
print(a2.shape)

a2sqz = a2.squeeze
print(a2sqz)


# # 사용자가 원하는대로 shape을 변경할 수 있음
# x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(x.view(3, 3))
# print(x.view(3, 1, 3))
# # print(x.view(4, 2)) <- shape의 크기를 고려하여 코드를 작성하지 않으면 error 발생

# w = torch.randn(3, 3)   # 랜덤한 값이 들어간 3 x 3 크기의 tensor를 생성 / 퍙균이 0 / 표준편차가 1
# print(w)
# b = torch.zeros(1)  
# print(b)                # tensor를 생성 (값은 모두 0으로 채움)
# h = torch.mm(x, w) + b  # wx + b 를 구할 수 있음 | mm을 통해서 matrix 곱을 할 수 있음


# Torch를 기울기 구하기
w = torch.tensor(1.0, requires_grad=True)
a = w * 3
l = a ** 2
l.backward()
print(w.grad)

x = torch.tensor(5.0, requires_grad=True)
y = 3 * x ** 3 + 4 * x + 7
y.backward()
print(x.grad)