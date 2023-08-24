import os

class FileRemover:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def remove_files(self):
        # Check if the folder exists
        if not os.path.exists(self.folder_path):
            print(f'The folder {self.folder_path} does not exist.')
            return

        # Get the list of files in the folder
        files = os.listdir(self.folder_path)

        if not files:
            print(f'The folder {self.folder_path} is empty.')
            return

        # Remove all files in the folder
        for file in files:
            file_path = os.path.join(self.folder_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f'Removed the file: {file_path}')

if __name__ == '__main__':
    # Example usage
    folder_path = 'folder_path'
    file_remover = FileRemover(folder_path)
    file_remover.remove_files()