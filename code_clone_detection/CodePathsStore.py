#!/usr/bin/python

from os import path, walk
from .ASTPath import ASTPath
from .suffix_tree import SuffixTree
import pickle

class CodePathsStore:

  def __init__(self, codebase_path, file_extension):
    self.codebase_path = codebase_path
    self.file_extension = file_extension

    self.paths = self.get_code_paths()

  def make_code_paths_for_directory(self):
    for root, dirs, files in walk(self.codebase_path):
      for filename in files:
        if filename.endswith(self.file_extension):
          if not path.isfile(self.cdp_file(root, filename)):
            self.make_code_paths_from_file(root, filename)

  def make_code_paths_from_file(self, root, filename):
    filename_path = path.join(root, filename)
    filepaths = ASTPath(filename_path, self.file_extension).paths
    string_paths = "".join(filepaths)
    with open(self.cdp_file(root, filename), 'wb') as f:
      pickle.dump(SuffixTree(string_paths), f)

  def get_code_paths(self):
    self.make_code_paths_for_directory()
    paths = {}

    for root, dirs, files in walk(self.codebase_path):
      for filename in files:
        cdp_filename = self.cdp_file(root, filename)
        if filename.endswith(self.file_extension):
          if path.isfile(cdp_filename):
            with open(cdp_filename, 'rb') as f:
              paths[path.join(root, filename)] = pickle.load(f)

    return paths

  def cdp_file(self, root, filename):
    return path.join(root, "."+filename+".cdp")
