import numpy as np

class CNN:
    def __init__(self, input_shape, num_filters, filter_size, num_classes):
        self.input_shape = input_shape
        self.num_filters = num_filters
        self.filter_size = filter_size
        self.num_classes = num_classes
        
        # Inicializa os filtros da camada convolucional
        self.filters = np.random.randn(num_filters, filter_size, filter_size) / (filter_size**2)
        
        # Calcula as dimensões da saída da camada de pooling
        self.pool_output_size = (input_shape[0] - filter_size + 1) // 2  # Assumindo pool_size=2 e stride=2
        self.flattened_size = num_filters * (self.pool_output_size ** 2)
        
        # Inicializa os pesos da camada totalmente conectada
        self.weights = np.random.randn(self.flattened_size, num_classes) / 100
        self.bias = np.zeros(num_classes)

    def convolution(self, input_image):
        output_size = self.input_shape[0] - self.filter_size + 1
        conv_output = np.zeros((self.num_filters, output_size, output_size))
        
        for f in range(self.num_filters):
            for i in range(output_size):
                for j in range(output_size):
                    region = input_image[i:i+self.filter_size, j:j+self.filter_size]
                    conv_output[f, i, j] = np.sum(region * self.filters[f])
        
        return conv_output

    def pooling(self, input_feature_map, pool_size=2, stride=2):
        num_filters, input_size, _ = input_feature_map.shape
        output_size = input_size // pool_size
        pooled_output = np.zeros((num_filters, output_size, output_size))
        
        for f in range(num_filters):
            for i in range(output_size):
                for j in range(output_size):
                    region = input_feature_map[f, i*stride:i*stride+pool_size, j*stride:j*stride+pool_size]
                    pooled_output[f, i, j] = np.max(region)
        
        return pooled_output

    def forward(self, input_image):
        conv_output = self.convolution(input_image)
        pooled_output = self.pooling(conv_output)
        flattened_output = pooled_output.flatten()
        logits = np.dot(flattened_output, self.weights) + self.bias
        return np.argmax(logits)



# Test Case para ajustar entradas e parâmetros
np.random.seed(42)  # Garante resultados consistentes
input_image = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # Imagem 3x3 fixa
cnn = CNN(input_shape=(3, 3), num_filters=1, filter_size=2, num_classes=10)

# Configurando filtros e pesos fixos para garantir resultado determinístico
cnn.filters = np.random.randn(1, 2, 2)
cnn.weights = np.random.randn(1 * 1, 10) / 100  # Ajuste do tamanho dos pesos

# Classe prevista
predicted_class = cnn.forward(input_image)
print("Classe prevista:", predicted_class)
'''
	
# Test Case 1: Imagem 4x4
np.random.seed(40) # Garante resultados consistentes
input_image = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])  # Imagem 4x4
cnn = CNN(input_shape=(4, 4), num_filters=2, filter_size=2, num_classes=3)

# Configurando filtros e pesos fixos para garantir resultado determinístico
cnn.filters = np.random.randn(2, 2, 2)
cnn.weights = np.random.randn(2 * 1, 3) / 100  # Ajuste do tamanho dos pesos

# Classe prevista
predicted_class = cnn.forward(input_image)
print("Classe prevista:", predicted_class)


# Test Case 3: Imagem 6x6
np.random.seed(43) # Garante resultados consistentes

input_image = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36]])  # Imagem 6x6
cnn = CNN(input_shape=(6, 6), num_filters=1, filter_size=2, num_classes=2)

# Configurando filtros e pesos fixos para garantir resultado determinístico
cnn.filters = np.random.randn(1, 2, 2)
cnn.weights = np.random.randn(1 * 4, 2) / 100  # Ajuste do tamanho dos pesos

# Classe prevista
predicted_class = cnn.forward(input_image)
print("Classe prevista:", predicted_class)

 Test Case 4: Imagem 3x3 com mais filtros
np.random.seed(41) # Garante resultados consistentes

input_image = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # Imagem 3x3
cnn = CNN(input_shape=(3, 3), num_filters=2, filter_size=2, num_classes=5)

# Configurando filtros e pesos fixos para garantir resultado determinístico
cnn.filters = np.random.randn(2, 2, 2)
cnn.weights = np.random.randn(2 * 1, 5) / 100  # Ajuste do tamanho dos pesos

# Classe prevista
predicted_class = cnn.forward(input_image)
print("Classe prevista:", predicted_class)

# Test Case 5: Imagem 6x6 com mais filtros
np.random.seed(42) # Garante resultados consistentes

input_image = np.array([
    [0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
    ])  # Imagem 6x6
cnn = CNN(input_shape=(6, 6), num_filters=1, filter_size=3, num_classes=5)

# Configurando filtros e pesos fixos para garantir resultado determinístico
cnn.filters = np.array([
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
])

cnn.weights = np.random.randn(1 * 4, 5) / 100  # Ajuste do tamanho dos pesos

# Classe prevista
predicted_class = cnn.forward(input_image)
print("Classe prevista:", predicted_class)


	
# Test Case 6: Imagem 6x6 com mais filtros
np.random.seed(42) # Garante resultados consistentes

input_image = np.array([
    [1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0],
    ])  # Imagem 6x6
cnn = CNN(input_shape=(6, 6), num_filters=2, filter_size=3, num_classes=5)

# Configurando filtros e pesos fixos para garantir resultado determinístico
cnn.filters = np.array([[
    [-1, 1, -1],
    [-1, 1, -1],
    [-1, 1, -1]],
    [[1, -1, -1],
    [-1, 1, -1],
    [-1, -1, 1]]]
    )

cnn.weights = np.random.randn(2 * 4, 5) / 100  # Ajuste do tamanho dos pesos

# Classe prevista
predicted_class = cnn.forward(input_image)
print("Classe prevista:", predicted_class)

'''