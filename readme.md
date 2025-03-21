### Deep learning
1. 向量化与矩阵话
- [线性回归的向量化 - 前向传播] 
z = w^T * x + b
z = w1*x1 + w2*x2 + w3*x3 + ... + b (一个神经元)

非向量化
for i in range(n):
    z += w[i] * x[i]
z += b

向量化
w_t = w.T
z = np.dot(w_t, x) + b


- [逻辑回归的向量化- 前向传播] 
z(1) = w^T * x(1) + b
a(1) = sigmoid(z(1))

z(2) = w^T * x(2) + b
a(2) = sigmoid(z(2))

z(3) = w^T * x(3) + b (3个样本)
a(3) = sigmoid(z(3))

使用矩阵代表x (n行m列)
X = [x1 x2 x3]

w^T * X + [b b ... b] = [z1 z2 z3 ..z(m)] = z
z = np.dot(w.T, X) + b
a = sigmoid(z) = 1 / (1 + np.exp(-z))


- [逻辑回归的矩阵化 - 多个神经元 - 前向传播] 
使用矩阵代表X (n行m列)
X = [x1 x2 x3]

使用矩阵代表W (n行k列) 代表每层神经的权重
W = [w1 w2 w3]

Z = np.dot(W.T, X) + b
A = relu(Z)

- [逻辑回归的矩阵化 - 多个神经元 - 反向传播] 
损失函数(L)关于w的偏导：

偏导/偏导(w) L(w, b)
偏导(L)/偏导(z) = sigma - y(i) = a - y(i)
* σ sigma
* 𝛿 偏导
* d 梯度

dZ = [dz(1) dz(2) dz(3) ... dz(m)]
A = [a(1) a(2) a(3) ... a(m)]
Y = [y(1) y(2) y(3) ... y(m)]
dZ = A - Y = [a(1) - y(1) a(2) - y(2) a(3) - y(3) ... a(m) - y(m)]

计算w和b的梯度:
dB = 1/m * np.sum(dZ)
dW = 1/m * np.dot(dZ, X)

2. L2正则化 (ridge)
* L1 is lasso 过时了
* 模型参数分布更加均匀和平滑
* 解决过拟合问题，修改某些特征值的权重为0
e.g., J(w, b) = 1/2m Σ(m, i=1) (f(i, (w,b)(x^i) - y(i)) ^ 2) + 10000 * w4
为了让10000 * w4接近于0，w4为很小的数，惩罚w4权重

=> L2的代价函数
J(w, b) = 1/2m Σ(m, i=1) (f(i, (w,b)(x^i) - y(i)) ^ 2) + lambda / 2m * Σ(n, j=1) w(j) ^ 2

""" 正则化w
lambda / 2m * Σ(n, j=1) w(j) ^ 2
"""
* 防止梯度消失: 每次更新参数前先减少一点w，再做梯度下降

3. Dropout正则化
* L2 在复杂的神经网络中还是会出现“过拟合问题”，所以我们使用dropout
* 随机丢弃一部分神经元，防止过拟合
* 输入层一般不使用dropout
* 隐藏层设置50%的比例 (20-40% 小的模型)
* 输出层不设置dropout

4. 数据归一化处理 (Normalization)
* 先对数据做均值处理, 求标准差, 最后归一化
* 防止梯度下降的时候震荡，代价函数比较平滑，达到"快速收敛"的目标

5. 初始化权重参数
* 0初始化，导致梯度消失问题
* 随机初始化，导致梯度消失问题
* Xavier初始化 - sigmoid / tanh
* He初始化 - relu

6. 全批量梯度下降
* 优点是梯度准确
* 缺点是计算量大，需要大内存

7. 随机梯度下降
* SGD
* 收敛不稳定，容易出现抖动

8. 小批量梯度下降 (* 普遍使用)
* 分批次训练，每次训练一个批次
* 收敛比较稳定
* 引入了超参数 mini-batch size，设置不好的话也会引起梯度下降剧烈震荡

9. 参数优化
* 动量梯度下降: 参考历史梯度来平滑梯度
* RMSProp: 调整学习率
* Adam = Momentum + RMSProp

10. BatchNormalization
* 每一层都进行归一化 (隐藏层)


ref: https://coding.imooc.com/learn/list/913.html