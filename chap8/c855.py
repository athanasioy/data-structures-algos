"""
Exercise P-4.27 described the walk function of the os module. This function
performs a traversal of the implicit tree represented by the file system.
Read the formal documentation for the function, and in particular its use
of an optional Boolean parameter named topdown. Describe how its behavior
relates to tree traversal algorithms described in this chapter.


Answer:
os walk function creates a generator that 'walks' through every
file and directory in a specified folder. Since file systems are
tree structures, os walk effectively does a tree traversal of the file
system.

the function takes an optional boolean parameter named 'topdown'. If
the specified parameter is set to true, the os walk functions allows
the caller of the function to modify the child directories that the
traversal will continue. This is akin to a preorder traversal where
the parent node gets visited first and the children. When the 'topdown'
parameter is set to false, the ability to define the child directories
that the traversal will visit is lost. This is akin to a postorder
traversal of a tree, where the children are visited first and then the
parent, effectively not "giving a chance" for the visited parent to
define which children should be traversed.


"""
