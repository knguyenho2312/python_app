from Library.c_Database import * 

class CD(Database):
    def __init__(self, path_db):
        self.conn = sqlite3.connect(path_db)
    
    def doc_danh_sach_cd(self):
        chuoi_sql = 'SELECT * FROM CD ORDER BY ID DESC '
        thong_tin = Database.get_all(self, chuoi_sql)
        return thong_tin
        
    

    def them_cd(self, Maso, ten_cd, ca_si, so_bai_hat, gia_thanh):
        chuoi_sql="Select * from CD Where Maso=? "
        cursor = Database.get_one(self, chuoi_sql,(Maso,))
        print(cursor)   
        if cursor!=None:	
            kq =0
        else:
            chuoi_sql = """INSERT INTO CD(MaSo, ten_cd, ca_si, so_bai_hat, gia_thanh) 
			VALUES (?, ?, ?, ?, ?)"""
            kq = Database.execute_q(self, chuoi_sql, (Maso, ten_cd, ca_si, so_bai_hat, gia_thanh))
            print("kq = ", kq)
            return kq




