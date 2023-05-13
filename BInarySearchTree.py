class Node:
    def __init__(self, name, is_file=False):
        self.name = name
        self.is_file = is_file
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)


class FileSystem:
    def  __init__(self):
        self.root = Node("root")

    def create_directory(self, path):
        # Split the path into directories
        directories = path.split("/")

        # Traverse the tree and create directories as needed
        node = self.root
        for directory in directories:
            # Check if the directory already exists
            for child in node.children:
                if child.name == directory:
                    node = child
                    break
            else:
            # If the directory doesn't exist, create a new node
                new_node = Node(directory)
                node.add_child(new_node)
                node = new_node
    
     def create_file(self, path):
        # Split the path into directories and filename
        directories, filename = path.rsplit("/", 1)

    # Traverse the tree and create directories as needed
        node = self.root
        for directory in directories.split("/"):
            # Check if the directory already exists
            for child in node.children:
                if child.name == directory:
                    node = child
                    break
            else:
                # If the directory doesn't exist, raise an exception
                raise ValueError("Directory does not exist")
            
         # Check if the file already exists
        for child in node.children:
            if child.name == filename:
                raise ValueError("File already exists")
        # Create a new file node and add it to the directory
        file_node = Node(filename, is_file=True)
        node.add_child(file_node)