import wx 
from UI.gd_doc_cd import * 
app = wx.App()
frame = wx.Frame(None, title = "Đọc CD - Bài thi cuối khóa", size = (700, 550), pos = (550, 450))

cd = CD(duong_dan_cd)
list_Cd = cd.doc_danh_sach_cd

panel = QL_CD(frame)

panel.m_listCtrl1.InsertColumn(0, 'ID', width = 70)
panel.m_listCtrl1.InsertColumn(1, 'Mã số', wx.LIST_FORMAT_LEFT, 150)
panel.m_listCtrl1.InsertColumn(2, 'Chủ đề', wx.LIST_FORMAT_LEFT, 200)
panel.m_listCtrl1.InsertColumn(3, 'Tên ca sĩ', wx.LIST_FORMAT_LEFT, 150)

frame.Show()
app.MainLoop()
