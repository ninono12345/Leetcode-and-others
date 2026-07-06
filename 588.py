# LeetCode didn't require to handle invalid-path errors!

from typing import List


class FileSystem:

    def __init__(self):
        self.folders_and_files = {}

    def ls(self, path: str) -> List[str]:
        paths = path.split("/")
        if paths[-1] == "":
            paths = paths[:-1]
        print("p", len(paths), paths)
        curr_path = self.folders_and_files

        for i in range(len(paths)):
            if i == len(paths)-1:
                print([k for k in curr_path])
                return [k for k in curr_path]

            curr_path = curr_path[paths[i]]

            # if paths[i] not in curr_path:
                # curr_path[paths[i]] = {}
                # curr_path = curr_path[paths[i]]

    def mkdir(self, path: str) -> None:
        paths = path.split("/")[1:]
        if paths[-1] == "":
            paths = paths[:-1]
        curr_path = self.folders_and_files

        for i in range(len(paths)):
            # if paths[i] == "":
            #     continue

            # if paths[i]

            if paths[i] not in curr_path:
                curr_path[paths[i]] = {}
            curr_path = curr_path[paths[i]]
        
        print(self.folders_and_files)

    def addContentToFile(self, filePath: str, content: str) -> None:
        paths = filePath.split("/")[1:]
        if paths[-1] == "":
            paths = paths[:-1]
        curr_path = self.folders_and_files

        for i in range(len(paths)):
            if i == len(paths)-1:
                curr_path[paths[i]] = content
                break

            curr_path = curr_path[paths[i]]
        # pass

    def readContentFromFile(self, filePath: str) -> str:
        # pass
        paths = filePath.split("/")[1:]
        curr_path = self.folders_and_files

        for i in range(len(paths)):
            if i == len(paths)-1:
                print(curr_path[paths[i]])
                break

            curr_path = curr_path[paths[i]]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath, content)
# param_2 = obj.readContentFromFile(filePath)


# AI generated edge cases test list
tests = [
  {
    "name": "empty_root_ls",
    "note": "Fresh system: root exists and is empty. ls('/') must return [], not error.",
    "methods": ["FileSystem", "ls"],
    "args": [[], ["/"]],
    "expected": [None, []]
  },
  {
    "name": "mkdir_root_is_noop",
    "note": "mkdir('/') splits to no components; root already exists. Must be a harmless no-op, not a crash or a phantom entry.",
    "methods": ["FileSystem", "mkdir", "ls"],
    "args": [[], ["/"], ["/"]],
    "expected": [None, None, []]
  },
  {
    "name": "single_mkdir",
    "note": "Most basic create. Dir shows up in parent; the new dir itself is empty.",
    "methods": ["FileSystem", "mkdir", "ls", "ls"],
    "args": [[], ["/a"], ["/"], ["/a"]],
    "expected": [None, None, ["a"], []]
  },
  {
    "name": "deep_mkdir_all_intermediates",
    "note": "Single mkdir of a deep path must create every intermediate directory. Check each level exists.",
    "methods": ["FileSystem", "mkdir", "ls", "ls", "ls", "ls"],
    "args": [[], ["/a/b/c"], ["/"], ["/a"], ["/a/b"], ["/a/b/c"]],
    "expected": [None, None, ["a"], ["b"], ["c"], []]
  },
  {
    "name": "mkdir_idempotent_nondestructive",
    "note": "Classic bug: re-mkdir of an existing dir must NOT wipe its children. /a gets child b, then mkdir /a again, b must survive.",
    "methods": ["FileSystem", "mkdir", "mkdir", "mkdir", "ls"],
    "args": [[], ["/a"], ["/a/b"], ["/a"], ["/a"]],
    "expected": [None, None, None, None, ["b"]]
  },
  {
    "name": "mkdir_partial_reuse",
    "note": "Part of the path already exists; mkdir must walk into it and only create the missing tail (c, d).",
    "methods": ["FileSystem", "mkdir", "mkdir", "ls", "ls"],
    "args": [[], ["/a/b"], ["/a/b/c/d"], ["/a/b"], ["/a/b/c"]],
    "expected": [None, None, None, ["c"], ["d"]]
  },
  {
    "name": "ls_is_non_recursive",
    "note": "ls returns ONLY immediate children, never descendants. With /a/b and /a/c/d, ls('/a') is [b,c] — d must NOT appear.",
    "methods": ["FileSystem", "mkdir", "mkdir", "ls", "ls"],
    "args": [[], ["/a/b"], ["/a/c/d"], ["/a"], ["/a/c"]],
    "expected": [None, None, None, ["b", "c"], ["d"]]
  },
  {
    "name": "addContent_creates_file_and_parents",
    "note": "addContentToFile on a nonexistent deep path creates all parent dirs AND the file. Mirrors the LeetCode example.",
    "methods": ["FileSystem", "addContentToFile", "ls", "ls", "readContentFromFile"],
    "args": [[], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c"], ["/a/b/c/d"]],
    "expected": [None, None, ["a"], ["d"], "hello"]
  },
  {
    "name": "addContent_file_at_root",
    "note": "File created directly under root. ls('/') lists it; ls on the file path returns just its name; content reads back.",
    "methods": ["FileSystem", "addContentToFile", "ls", "ls", "readContentFromFile"],
    "args": [[], ["/f", "x"], ["/"], ["/f"], ["/f"]],
    "expected": [None, None, ["f"], ["f"], "x"]
  },
  {
    "name": "append_to_existing",
    "note": "Second addContentToFile on an existing file APPENDS rather than overwrites.",
    "methods": ["FileSystem", "addContentToFile", "addContentToFile", "readContentFromFile"],
    "args": [[], ["/f", "hello"], ["/f", " world"], ["/f"]],
    "expected": [None, None, None, "hello world"]
  },
  {
    "name": "many_appends_preserve_order",
    "note": "Multiple appends concatenate in call order: a + b + c = abc.",
    "methods": ["FileSystem", "addContentToFile", "addContentToFile", "addContentToFile", "readContentFromFile"],
    "args": [[], ["/x", "a"], ["/x", "b"], ["/x", "c"], ["/x"]],
    "expected": [None, None, None, None, "abc"]
  },
  {
    "name": "empty_content_file_exists",
    "note": "A file created with empty content still EXISTS. read returns ''; ls('/') must show it (distinguishes empty file from no file).",
    "methods": ["FileSystem", "addContentToFile", "readContentFromFile", "ls"],
    "args": [[], ["/f", ""], ["/f"], ["/"]],
    "expected": [None, None, "", ["f"]]
  },
  {
    "name": "append_empty_string_noop",
    "note": "Appending '' to an existing file leaves content unchanged.",
    "methods": ["FileSystem", "addContentToFile", "addContentToFile", "readContentFromFile"],
    "args": [[], ["/f", "abc"], ["/f", ""], ["/f"]],
    "expected": [None, None, None, "abc"]
  },
  {
    "name": "addContent_reuses_existing_dirs",
    "note": "Dirs made by mkdir, then a file added inside them. File creation must walk INTO existing dirs, not clobber the tree.",
    "methods": ["FileSystem", "mkdir", "addContentToFile", "ls", "readContentFromFile"],
    "args": [[], ["/a/b"], ["/a/b/f", "data"], ["/a/b"], ["/a/b/f"]],
    "expected": [None, None, None, ["f"], "data"]
  },
  {
    "name": "content_with_spaces_preserved",
    "note": "Content is an arbitrary string; internal spaces are preserved verbatim (not trimmed or split).",
    "methods": ["FileSystem", "addContentToFile", "readContentFromFile"],
    "args": [[], ["/f", "a b  c   d"], ["/f"]],
    "expected": [None, None, "a b  c   d"]
  },
  {
    "name": "ls_on_file_returns_name_shallow",
    "note": "ls on a one-level-deep file returns [filename], the file's own name only.",
    "methods": ["FileSystem", "addContentToFile", "ls"],
    "args": [[], ["/a/b", "x"], ["/a/b"]],
    "expected": [None, None, ["b"]]
  },
  {
    "name": "ls_on_file_returns_name_deep",
    "note": "Same fork, but file is deep. ls('/a/b/c/d') returns ['d'] (last component), not the path or parent's listing.",
    "methods": ["FileSystem", "addContentToFile", "ls"],
    "args": [[], ["/a/b/c/d", "val"], ["/a/b/c/d"]],
    "expected": [None, None, ["d"]]
  },
  {
    "name": "ls_sorts_not_insertion",
    "note": "Inserted z, a, m; ls must return lexicographically sorted [a, m, z], proving it sorts rather than echoing insertion order.",
    "methods": ["FileSystem", "mkdir", "mkdir", "mkdir", "ls"],
    "args": [[], ["/z"], ["/a"], ["/m"], ["/"]],
    "expected": [None, None, None, None, ["a", "m", "z"]]
  },
  {
    "name": "ls_mixed_files_dirs_sorted",
    "note": "Files and directories sort together as plain names, ignoring type: dir d, file a, dir c, file b -> [a, b, c, d].",
    "methods": ["FileSystem", "mkdir", "addContentToFile", "mkdir", "addContentToFile", "ls"],
    "args": [[], ["/d"], ["/a", "1"], ["/c"], ["/b", "2"], ["/"]],
    "expected": [None, None, None, None, None, ["a", "b", "c", "d"]]
  },
  {
    "name": "ls_lexicographic_prefix",
    "note": "THE classic gotcha. b, ab, a must sort to [a, ab, b] (shorter prefix before its extension). Catches sort-by-length bugs.",
    "methods": ["FileSystem", "mkdir", "mkdir", "mkdir", "ls"],
    "args": [[], ["/b"], ["/ab"], ["/a"], ["/"]],
    "expected": [None, None, None, None, ["a", "ab", "b"]]
  },
  {
    "name": "file_and_dir_shared_prefix",
    "note": "File 'a' and dir 'ab' coexist with a shared prefix. ls('/') -> [a, ab]; ls('/a') -> [a] (file fork); ls('/ab') -> [] (empty dir fork).",
    "methods": ["FileSystem", "addContentToFile", "mkdir", "ls", "ls", "ls"],
    "args": [[], ["/a", "x"], ["/ab"], ["/"], ["/a"], ["/ab"]],
    "expected": [None, None, None, ["a", "ab"], ["a"], []]
  },
  {
    "name": "ls_fork_file_vs_dir_same_parent",
    "note": "Inside one parent: a subdir and a file. ls(parent) lists both sorted; ls(file) -> [name]; ls(empty subdir) -> [].",
    "methods": ["FileSystem", "mkdir", "mkdir", "addContentToFile", "ls", "ls", "ls"],
    "args": [[], ["/a"], ["/a/sub"], ["/a/file", "hi"], ["/a"], ["/a/file"], ["/a/sub"]],
    "expected": [None, None, None, None, ["file", "sub"], ["file"], []]
  },
  {
    "name": "sibling_branches",
    "note": "Two children created under the same dir via separate deep mkdirs; both must appear, sorted.",
    "methods": ["FileSystem", "mkdir", "mkdir", "ls"],
    "args": [[], ["/a/b"], ["/a/c"], ["/a"]],
    "expected": [None, None, None, ["b", "c"]]
  },
  {
    "name": "kitchen_sink_complex",
    "note": "End-to-end persistence check: nested mkdir, append, mixed sorted ls, ls-on-file, NON-destructive re-mkdir, fresh deep auto-create, root listing.",
    "methods": ["FileSystem", "mkdir", "mkdir", "addContentToFile", "addContentToFile", "mkdir", "addContentToFile", "ls", "ls", "ls", "readContentFromFile", "mkdir", "ls", "addContentToFile", "ls", "ls", "readContentFromFile"],
    "args": [[], ["/usr"], ["/usr/local"], ["/usr/local/notes", "hello"], ["/usr/local/notes", " world"], ["/usr/bin"], ["/usr/readme", "top"], ["/usr"], ["/usr/local"], ["/usr/local/notes"], ["/usr/local/notes"], ["/usr/local"], ["/usr/local"], ["/a/b/c/deep", "x"], ["/"], ["/a/b/c"], ["/a/b/c/deep"]],
    "expected": [None, None, None, None, None, None, None, ["bin", "local", "readme"], ["notes"], ["notes"], "hello world", None, ["notes"], None, ["a", "usr"], ["deep"], "x"]
  }
]

for d in tests:
    obj = FileSystem()
    continued = False
    for m, a, e in zip(d["methods"], d["args"], d["expected"]):
        if not continued:
            continued=True
            continue
        
        if m=="ls":
            assert obj.ls(a[0]) == e
        if m=="mkdir":
            assert obj.mkdir(a[0]) == e
        if m=="addContentToFile":
            assert obj.addContentToFile(a[0], a[1]) == e
        if m=="readContentFromFile":
            assert obj.readContentFromFile(a[0]) == e

    print(d["name"], "good")