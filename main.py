import zipfile


class DocXImageRename:
    """
    To extract and rename images inside an unzipped DocX file.
    """

    def __init__(self, dir_name: str, dir_out: str, rename_as: str, file_type='jpg', max_size=1) -> None:

        self.dir_name = dir_name
        self.dir_out = dir_out
        self.rename = rename_as
        self.max_size = max_size
        self.file_type = file_type

    def extract_files(self):
        count = 1
        archive = zipfile.ZipFile(self.dir_name)
        for file in archive.filelist:
            if file.filename.startswith('word/media/') and file.file_size > self.max_size:
                file.filename = f"{self.dir_out}/{self.rename}{count}.{self.file_type}"
                archive.extract(file)
                count += 1
        print(f"Extracted {count} images.")
        return True
