from Library.c_CD import *
from Library.xl_chung import * 

import wx
import wx.xrc


class QL_CD ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 723,436 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Thêm thông tin CD", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 18, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Times New Roman" ) )
		self.m_staticText1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer1.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"D:\\HoNguyenKhoiNguyen\\Images\\Bia_CD.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.m_bitmap1, wx.GBPosition( 0, 0 ), wx.GBSpan( 6, 1 ), wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Mã số CD: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		gbSizer1.Add( self.m_staticText2, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Tên CD: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		gbSizer1.Add( self.m_staticText4, wx.GBPosition( 1, 7 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		gbSizer1.Add( self.m_textCtrl3, wx.GBPosition( 1, 9 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Tên ca sĩ: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		gbSizer1.Add( self.m_staticText5, wx.GBPosition( 2, 7 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		gbSizer1.Add( self.m_textCtrl1, wx.GBPosition( 0, 9 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		gbSizer1.Add( self.m_textCtrl4, wx.GBPosition( 2, 9 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Số bài hát: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		gbSizer1.Add( self.m_staticText6, wx.GBPosition( 3, 7 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		gbSizer1.Add( self.m_textCtrl5, wx.GBPosition( 3, 9 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Giá thành: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		gbSizer1.Add( self.m_staticText7, wx.GBPosition( 4, 7 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		gbSizer1.Add( self.m_textCtrl6, wx.GBPosition( 4, 9 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.btn_doc = wx.Button( self, wx.ID_ANY, u"Đọc danh sách CD", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.btn_doc, wx.GBPosition( 5, 7 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.btn_them = wx.Button( self, wx.ID_ANY, u"Thêm", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.btn_them, wx.GBPosition( 5, 9 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		bSizer1.Add( gbSizer1, 1, wx.EXPAND, 5 )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.m_listCtrl1 = wx.ListCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 700,-1 ), wx.LC_REPORT )
		sbSizer2.Add( self.m_listCtrl1, 0, wx.ALL, 5 )


		bSizer1.Add( sbSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		# Connect Events
		self.btn_doc.Bind( wx.EVT_BUTTON, self.doc_onclicked )
		self.btn_them.Bind( wx.EVT_BUTTON, self.them_onclicked )

	def __del__( self ):
		pass
	

	# Virtual event handlers, override them in your derived class
	def doc_onclicked( self, event ):
		self.m_listCtrl1.DeleteAllItems()
		cd = CD(duong_dan_cd)
		kq = cd.doc_danh_sach_cd()
		if len(kq)>0:
			index = 0
			for dong in kq:
				self.m_listCtrl1.InsertItem(index, dong[0])
				self.m_listCtrl1.SetItem(index,0, str(dong[0]))
				self.m_listCtrl1.SetItem(index,1, dong[1])
				self.m_listCtrl1.SetItem(index,2, dong[2])
				self.m_listCtrl1.SetItem(index,3, dong[3])
		else:
			wx.MessageBox("Không có CD theo điều kiện cần tìm", 'Thông báo', wx.OK | wx.ICON_INFORMATION)


	def them_onclicked( self, event ):
		maCD = self.m_textCtrl1.GetValue()
		tenCD = self.m_textCtrl3.GetValue()
		ten_ca_si = self.m_textCtrl4.GetValue()
		so_bai_hat = self.m_textCtrl5.GetValue()
		gia_thanh = self.m_textCtrl6.GetValue()
		if maCD == "" or tenCD == "" or ten_ca_si == "": 
			wx.MessageBox("Bạn chưa đủ thông tin ", 'Thông báo', wx.OK | wx.ICON_ERROR)
			self.m_textCtrl1.SetFocus()
			return
		cd = CD(duong_dan_cd)
		kq = cd.them_cd(maCD, tenCD, ten_ca_si, so_bai_hat, gia_thanh)
		if kq != 0:
			self.m_textCtrl1.SetValue("")
			self.m_textCtrl3.SetValue("")
			self.m_textCtrl4.SetValue("")
			self.m_textCtrl5.SetValue("")
			self.m_textCtrl6.SetValue("")
			wx.MessageBox("Thêm CD thành công", 'Thông báo', wx.OK | wx.ICON_INFORMATION)
		else:
			wx.MessageBox("Thêm CD thất bại ", 'Thông báo', wx.OK | wx.ICON_ERROR)
		