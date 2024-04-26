import torch

# Supposons que 'tensor1' et 'tensor2' sont vos tenseurs de même dimension
tensor1 = torch.tensor([[1, 2], [3, 4]])
tensor2 = torch.tensor([[5, 6], [7, 8]])

# Multiplier les termes à termes des deux tenseurs
result = tensor1 * tensor2

# Afficher le résultat
print(result)