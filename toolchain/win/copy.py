import os
import shutil
import sys

def main(args):
  if len(args) != 2:
    raise Exception("Wrong number of arguments")
  return RecursiveMirror(args[0], args[1])

def RecursiveMirror(source, dest):
  """Emulation of rm -rf out && cp -af in out."""
  if os.path.exists(dest):
    if os.path.isdir(dest):
      def _on_error(fn, path, dummy_excinfo):
        # The operation failed, possibly because the file is set to
        # read-only. If that's why, make it writable and try the op again.
        if not os.access(path, os.W_OK):
          os.chmod(path, stat.S_IWRITE)
        fn(path)
      shutil.rmtree(dest, onerror=_on_error)
    else:
      if not os.access(dest, os.W_OK):
        # Attempt to make the file writable before deleting it.
        os.chmod(dest, stat.S_IWRITE)
      os.unlink(dest)

  if os.path.isdir(source):
    shutil.copytree(source, dest)
  else:
    shutil.copy2(source, dest)
    # Try to diagnose crbug.com/741603
    if not os.path.exists(dest):
      raise Exception("Copying of %s to %s failed" % (source, dest))

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))