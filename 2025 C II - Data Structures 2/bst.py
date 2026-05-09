import collections

class Node:
    def __init__(self, i, n):
        self.idade = i
        self.nome = n
        self.leftLeaf = None
        self.rightLeaf = None

    def insert(self, i, n):
        if self.idade == i:
            # Considerando nome caso idades sejam iguais.
            if self.nome == n:
                if self.rightLeaf: #Inserir na direita caso os nomes também sejam iguais.
                    return self.rightLeaf.insert(i, n)
                else:
                    self.rightLeaf = Node(i, n)
            else:
                if self.leftLeaf: #Inserir na esquerda caso sejam diferentes.
                    return self.leftLeaf.insert(i, n)
                else:
                    self.leftLeaf = Node(i, n)

        elif self.idade > i:
            if self.leftLeaf:
                return self.leftLeaf.insert(i, n)
            else:
                self.leftLeaf = Node(i, n)
                return

        else:
            if self.rightLeaf:
                return self.rightLeaf.insert(i, n)
            else:
                self.rightLeaf = Node(i, n)
                return


    def inorder(self):
        if self:
            if self.leftLeaf:
                self.leftLeaf.inorder()
            print("Nome: ", self.nome, " - Idade: ", str(self.idade))
            if self.rightLeaf:
                self.rightLeaf.inorder()

    def preorder(self):
        if self:
            print("Nome: ", self.nome, "    - Idade: ", str(self.idade))
            if self.leftLeaf:
                self.leftLeaf.preorder()
            if self.rightLeaf:
                self.rightLeaf.preorder()
    
    def postorder(self):
        if self:
            if self.leftLeaf:
                self.leftLeaf.postorder()
            if self.rightLeaf:
                self.rightLeaf.postorder()
            print("Nome: ", self.nome, " - Idade: ", str(self.idade))
    
    def decorder(self):
        list = []
        if self:
            if self.rightLeaf:
                self.rightLeaf.decorder()
            print("Nome: ", self.nome, " - Idade: ", str(self.idade))
            if self.leftLeaf:
                self.leftLeaf.decorder()

class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, i, n):
        if self.root:
            return self.root.insert(i, n)
        else:
            self.root = Node(i, n)
    
    def inorder(self):
        print("\n\n##### In-Order #####\n")
        self.root.inorder()
    
    def preorder(self):
        print("\n\n##### Pre-Order #####\n")
        self.root.preorder()
    
    def postorder(self):
        print("\n\n##### Post-Order #####\n")
        self.root.postorder()
    
    def decorder(self):
        print("\n\n##### Dec-Order #####\n")
        self.root.decorder()
    
    def largura(self):
        print("\n\n##### Largura #####\n")
        total_tree = []
        queue = collections.deque()
        queue.append(self.root)

        while queue:
            queue_len = len(queue)
            level = []
            for node in range(queue_len): #Divide os Nodes em níveis
                node = queue.popleft()
                if node:
                    level.append(node)
                    queue.append(node.leftLeaf)
                    queue.append(node.rightLeaf)
            if level: #Adiciona os níveis na lista total
                total_tree.append(level)
        for level in total_tree: #Lê os Nodes por nível.
            for node in level:
                print("Nome: ", node.nome, " - Idade: ", str(node.idade))


bst = Tree()

bst.insert(10, "Joana")
bst.insert(12, "Pedro")
bst.insert(19, "Alice")
bst.insert(21, "Erick")
bst.insert(15, "Ellen")
bst.insert(15, "Henry")
bst.insert(24, "Vitor")
bst.insert(23, "Lenny")
bst.insert(18, "Maria")
bst.insert(20, "Sammy")

bst.inorder()
bst.preorder()
bst.postorder()
bst.decorder()
bst.largura()