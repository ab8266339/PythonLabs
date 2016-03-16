# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 15:01:44 2015

@author: Hao Xu
"""
def wordCounts(files):
    worddic={}
    in_fs=open(files)
    stopdic={}
    stops=open('stopwords.txt')
    for n in stops:
        n=n.strip()
        stopdic[n]=1
    print stopdic
    for line in in_fs:
        line=line.split()
    ##    word={}
    #    print n
    #    wordlist.append(n)
        for x in line:
            if x in stopdic:
                worddic[x]=0
    #        print x
            if x in worddic:
                worddic[x]+=1
            else:
                worddic[x]=1
    print worddic
def printTop20(files):
    worddic={}
    in_fs=open(files)
    stopdic={}
    stops=open('stopwords.txt')
    for n in stops:
        n=n.strip()
        stopdic[n]=1
#    print stopdic
    for line in in_fs:
        line=line.split()
        for x in line:
             if x in stopdic:
                worddic[x]=0
    #        print x
             elif x in worddic:
                worddic[x]+=1
             else:
                worddic[x]=1
    counts=worddic
    lables=counts.keys()
    lables.sort(reverse=True, key=lambda v:counts[v])  
#    print lables
    top=0    
    for n in lables:
        print n,'=',counts[n]
        top+=1
        if top ==20:
            break

def stops():
    stopdic={}
    stops=open('stopwords.txt')
    for n in stops:
#        print n
        n=n.strip()
        stopdic[n]=1
    print stopdic
stops()
def similarity(name):
    worddic={}
    name=[]
    for n in name:
        in_fs=open(n)
        stopdic={}
        stops=open('stopwords.txt')
        for n in stops:
            n=n.strip()
            stopdic[n]=1
        print stopdic
        for line in in_fs:
            line=line.split()
            for x in line:
                if x in stopdic:
                    worddic[x]=0
        #        print x
                if x in worddic:
                    worddic[x]+=1
                else:
                    worddic[x]=1
        print worddicd