import zipfile, os


def unzip(zpath, zfile):
    file_path = zpath + os.sep + zfile
    desdir = zpath + os.sep + zfile[:zfile.index('.zip')]
    srcfile = zipfile.ZipFile(file_path)
    for filename in srcfile.namelist():
        srcfile.extract(filename, desdir)
        if filename.endswith('.zip'):
            # if zipfile.is_zipfile(filename):
            zpath = desdir
            zfile = filename
            unzip(zpath, zfile)


zpath = r'E:\test'
zfile = r'entryTransaction.zip'
unzip(zpath, zfile)
