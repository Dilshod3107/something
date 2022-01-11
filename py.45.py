import sqlite3

class data:
      def create():
          baza=sqlite3.connect('database.db')
          amal=baza.cursor()
          amal.execute("""create table if not exists talabalar(id integer,
                                                                 ism text,
                                                                 familya text,
                                                                 sharif text,
                                                                 yosh integer,
                                                                 jinsi text,
                                                                 kurs integer)""")
          baza.commit()
          baza.close()             

      def insert(id,ism,familya,sharif,yosh,jinsi,kurs): 
           baza=sqlite3.connect('database.db')
           amal=baza.cursor()
           amal.execute(f"""insert into talabalar values({id},
                                                          "{ism}",
                                                          "{familya}",
                                                          "{sharif}",
                                                          {yosh},
                                                          "{jinsi}",
                                                          {kurs})""")
           baza.commit()
           baza.close()
           print('saqlandi!')
      def delete(id):
          baza=sqlite3.connect('database.db')
          amal=baza.cursor()
          amal.execute(f'delete from talabalar where id={id}')
          

          
          baza.commit()
          baza.close()
          print("o'chirildi!")
                                                          
                                                                 
