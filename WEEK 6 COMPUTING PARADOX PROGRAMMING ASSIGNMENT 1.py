"""QUESTION:-
You are provided with a playlist containing N songs, each has a unique positive integer length. Assume you like all the songs from this playlist, but there is a song, which you like more than others.
It is named "Computing Paradox".

You decided to sort this playlist in increasing order of songs length. For example, if the lengths of the songs in the playlist were {1, 3, 5, 2, 4} after sorting it becomes {1, 2, 3, 4, 5}.
Before the sorting, "Computing Paradox" was on the kth position (1-indexing is assumed for the playlist) in the playlist.

Your task is to find the position of "Computing Paradox" in the sorted playlist.

Input Format:
The first line contains two numbers N denoting the number of songs in the playlist.
The second line contains N space separated integers A1, A2, A3,..., AN denoting the lengths of songs.
The third line contains an integer k, denoting the position of "Computing Paradox" in the initial playlist.

Output Format:

Output a single line containing the position of "Computing Paradox" in the sorted playlist.

Example:

Input:
4
1 3 4 2
2

SOLUTION"""

x=int(input())
lis=[int(i) for i in input().split(" ")]
sort=sorted(lis)
#uploaded by ULTIMATE GAMER
k=int(input())
pos=lis[k-1]
if pos in sort:
  ind=sort.index(pos)+1
  print(ind,end='')
