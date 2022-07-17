# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class category_properties
###########################################################################

class category_properties ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Category Properties", pos = wx.DefaultPosition, size = wx.Size( 319,403 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Property of Category", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Microsoft YaHei UI" ) )

		bSizer4.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer4.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.display_category_name = wx.StaticText( self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.display_category_name.Wrap( -1 )

		bSizer4.Add( self.display_category_name, 0, wx.ALL, 5 )

		self.display_category_create_date = wx.StaticText( self, wx.ID_ANY, u"Create Date:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.display_category_create_date.Wrap( -1 )

		bSizer4.Add( self.display_category_create_date, 0, wx.ALL, 5 )

		self.display_category_location = wx.StaticText( self, wx.ID_ANY, u"Location:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.display_category_location.Wrap( -1 )

		bSizer4.Add( self.display_category_location, 0, wx.ALL, 5 )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer4.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Description for the Category:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer4.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.display_category_description = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer4.Add( self.display_category_description, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer4.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

		self.btn_modify = wx.Button( self, wx.ID_ANY, u"Modify This Category", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.btn_modify, 0, wx.ALL|wx.EXPAND, 5 )

		btn_ok = wx.StdDialogButtonSizer()
		self.btn_okOK = wx.Button( self, wx.ID_OK )
		btn_ok.AddButton( self.btn_okOK )
		btn_ok.Realize();

		bSizer4.Add( btn_ok, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.init_display_data )
		self.btn_modify.Bind( wx.EVT_BUTTON, self.modify_category )
		self.btn_okOK.Bind( wx.EVT_BUTTON, self.close_dialog )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def init_display_data( self, event ):
		event.Skip()

	def modify_category( self, event ):
		event.Skip()

	def close_dialog( self, event ):
		event.Skip()


