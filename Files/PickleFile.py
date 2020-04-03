import pickle


def writeToBinaryFile(fileName, repo):
    f = open(fileName, "wb")
    pickle.dump(repo.getAll(), f)
    f.close()
    

