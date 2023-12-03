#Jeffery James
class Node:
  def __init__(self,popularity, songID,artist, songName,genre,explicit):
    self.songName = songName
    self.genre = genre
    self.songID = songID
    self.artist = artist
    self.popularity = popularity
    self.explicit = explicit
    self.colorRed = False
    self.left = None
    self.right = None
    self.parent = None


class RedBlackTree:
  def __init__(self):
    self.leaf = Node(0,0,"name","title","genre",False)
    self.leaf.colorRed = False
    self.leaf.left = None
    self.leaf.right = None
    self.root = self.leaf
    self.songTray = []

  def insert(self,popularity,artist,songID,songName,genre,explicit):
    newNode = Node(popularity,songID,artist,songName,genre,explicit)
    newNode.parent = None
    newNode.left = self.leaf
    newNode.right = self.leaf
    newNode.colorRed = True
    self.insertNode(newNode)
    self.rbTreeBalance(newNode)



  def insertNode(self, node):
    #Inserts node into tree based on popularity
    parent = None
    current = self.root
    while current != self.leaf:
      parent = current
      if node.popularity < current.popularity:
        current = current.left
      else:
        current = current.right

    node.parent = parent
    if parent == None:
      self.root = node
    elif node.popularity < parent.popularity:
      parent.left = node
    else:
      parent.right = node
  
  def rbTreeBalance(self, node):
    #Balances tree using rb tree properties
    while node.parent is not None and node.parent.colorRed and node != self.root:
      #used to determine if if uncle is left or right node
      if node.parent == node.parent.parent.right:
        uncle = node.parent.parent.left
        if uncle.colorRed == True:
          uncle.colorRed = False
          node.parent.colorRed = False
          node.parent.parent.colorRed = True
          node = node.parent.parent
        else:
          if node == node.parent.left:
            node = node.parent
            self.rightRotate(node)
          node.parent.colorRed = False
          node.parent.parent.colorRed = True
          self.leftRotate(node.parent.parent)
      else:
        uncle = node.parent.parent.right

        if uncle.colorRed == True:
          uncle.colorRed = False
          node.parent.colorRed = False
          node.parent.parent.colorRed = True
          node = node.parent.parent
        else:
          if node == node.parent.right:
            node = node.parent
            self.leftRotate(node)
          node.parent.colorRed = False
          node.parent.parent.colorRed = True
          self.rightRotate(node.parent.parent)
      if node == self.root:
        break
    self.root.colorRed = False

  def leftRotate(self, node):
    rightNode = node.right
    node.right = rightNode.left
    if rightNode.left != self.leaf:
      rightNode.left.parent = node
    rightNode.parent = node.parent
    if node.parent == None:
      self.root = rightNode
    elif node == node.parent.left:
      node.parent.left = rightNode
    else:
      node.parent.right = rightNode
    rightNode.left = node
    node.parent = rightNode
  
  def rightRotate(self, node):
    leftNode = node.left
    node.left = leftNode.right
    if leftNode.right != self.leaf:
      leftNode.right.parent = node
    leftNode.parent = node.parent
    if node.parent == None:
      self.root = leftNode
    elif node == node.parent.right:
      node.parent.right = leftNode
    else:
      node.parent.left = leftNode
    leftNode.right = node
    node.parent = leftNode


  def __repr__(self):
        lines = []
        print_tree(self.root, lines)
        return '\n'.join(lines)
  
  def searchArtist(self,node, target_artist):
       #Searches for artist in tree if node has the artist or artist is not being filtered adds to songTray
       if node!= self.leaf:
        self.searchArtist(node.left, target_artist)
        if node.artist == target_artist or target_artist == '':
            self.songTray.append(node)
        self.searchArtist(node.right, target_artist)
  
  def searchGenre(self,node, target_genre):
       #Searches for genre in tree if node has the genre or genre is not being filtered adds to songTray
       if node!= self.leaf:
        self.searchGenre(node.left, target_genre)
        if node.genre == target_genre or target_genre == '':
            self.songTray.append(node)
        self.searchGenre(node.right, target_genre)
  
  def searchExplicit(self,node, target_explicit):
        #Searches for explicit in tree if node has the explicit or explicit is not being filtered adds to songTray
       if node != self.leaf:
        self.searchExplicit(node.left, target_explicit)
        if node.explicit == target_explicit or target_explicit == '':
            self.songTray.append(node)
        self.searchExplicit(node.right, target_explicit)

  def search(self,target_artist,target_genre,target_explicit,maxSongs):
    sortedArray = set()

    self.searchArtist(self.root,target_artist)
    self.searchExplicit(self.root,target_explicit)
    self.searchGenre(self.root,target_genre)

    for song in self.songTray:
        #Adds songs to sortedArray if they are in the songTray and the songTray is not full and the song hits all the filters
        if song.artist == target_artist or target_artist == '':
          if song.genre == target_genre or target_genre == '':
            if song.explicit == str(target_explicit) or target_explicit == 'True':
              if(len(sortedArray) < maxSongs):
                sortedArray.add(song.songID)
              elif(len(sortedArray) == maxSongs):
                break

    return sortedArray  



def print_tree(node, lines,level=0):
    if node.popularity != 0:
        print_tree(node.left, lines, level + 1)
        lines.append('-' * 4 * level + '> ' +
                     str(node.popularity)+ str(node.artist) + str(node.songName) + ' ' + ('r' if node.colorRed else 'b'))
        print_tree(node.right, lines, level + 1)
  
