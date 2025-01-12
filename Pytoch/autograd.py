import torch
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math

# a = torch.linspace(0., 2. * math.pi, steps=25, requires_grad=True)
# print(a)

# b = torch.sin(a)
# plt.plot(a.detach(), b.detach())

# print(b)
# c = 2 * b
# print(c)

# d = c + 1
# print(d)

# out = d.sum()
# print(out)

# print("d: ")
# print(d.grad_fn)
# print(d.grad_fn.next_functions)
# print(d.grad_fn.next_functions[0][0].next_functions)
# print(d.grad_fn.next_functions[0][0].next_functions[0][0].next_functions)
# print(d.grad_fn.next_functions[0][0].next_functions[0][0].next_functions[0][0].next_functions)
# print('\nc:')
# print(c.grad_fn)
# print('\nb:')
# print(b.grad_fn)
# print('\na:')
# print(a.grad_fn)


# out.backward()
# print(a.grad)
# plt.plot(a.detach(), a.grad.detach())

# a = torch.linspace(0., 2. * math.pi, steps=25, requires_grad=True)
# b = torch.sin(a)
# d = c + 1
# out = d.sum()

# AUTOGRAD
BATCH_SIZE = 16
DIM_IN = 1000
HIDDEN_SIZE = 100
DIM_OUT = 10

class TinyModel(torch.nn.Module):
    def __init__(self):
        super(TinyModel, self).__init__()

        self.layer1 = torch.nn.Linear(DIM_IN, HIDDEN_SIZE)
        self.relu = torch.nn.ReLU() # optimization
        self.layer2 = torch.nn.Linear(HIDDEN_SIZE, DIM_OUT)

    def forward(self, x):
        x = self.layer1(x)
        x = self.relu(x)
        x = self.layer2(x)

        return x

some_input = torch.randn(BATCH_SIZE, DIM_IN, requires_grad=False)
ideal_output = torch.randn(BATCH_SIZE, DIM_OUT, requires_grad=False)

# never specify requires_grad=True for the models layers. Within a subclass of torch.nn.Module, it's assumed
# that we want to track gradients on the layers'weight for learning

model = TinyModel()

# print(model.layer2.weight[0][0:10])

optimizer = torch.optim.SGD(model.parameters(), lr=0.001)
prediction = model(some_input)
loss = (ideal_output - some_input).pow(2).sum()
print(loss)

loss.backward()
print(model.layer2.weight[0][0:10])
print(model.layer2.weight.grad[0][0:10])

optimizer.step()
print(model.layer2.weight[0][0:10])
print(model.layer2.weight.grad[0][0:10])

print(model.layer2.weight.grad[0][0:10])

for i in range(0, 5):
    prediction = model(some_input)
    loss = (ideal_output - prediction).pow(2).sum()
    loss.backward()

print(model.layer2.weight.grad[0][0:10])

optimizer.zero_grad(set_to_none=False)

print(model.layer2.weight.grad[0][0:10])