import sqlite3
class Database :
    def __init__(self ,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()

        sql = """
        
        CREATE TABLE IF NOT EXISTS Stagiaire(
            N Integer Primary Key ,
            Name  text ,
            Filier text ,
            Sexe text ,
            CEF Integer ,
            Email text ,
            Id text ,
            Adress text 

        )
        """
        self.cur .execute(sql)
        self.con.commit()
    
    def insert (self, Name ,Filier ,Sexe ,CEF , Email , Id ,Adress) :
        self .cur.execute("insert into Stagiaire values (NULL ,?,?,?,?,?,?,?)",
        (Name ,Filier ,Sexe ,CEF , Email , Id ,Adress))
        
        self.con.commit()


    def fetch (self):
        self.cur.execute("SELECT * FROM Stagiaire ")
        rows = self.cur.fetchall()
        return rows
    
    def remove (self ,N) :
        self.cur.execute("delete from Stagiaire where N=? ",(N ,))
        self.con.commit()

    def update (self , N , Name ,Filier ,Sexe ,CEF , Email , Id ,Adress ) : 
        self.cur.execute("update Stagiaire set  Name = ? ,Filier =? ,Sexe =? ,CEF =? , Email =? , Id =? ,Adress =? where N = ? " ,
                    ( Name ,Filier ,Sexe ,CEF , Email , Id ,Adress , N ) )
        self.con.commit()