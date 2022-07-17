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
## Class settings
###########################################################################

class settings ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Union Project Settings", pos = wx.DefaultPosition, size = wx.Size( 322,372 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Passwor Protection Settings", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		self.m_staticText6.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Microsoft YaHei UI" ) )

		bSizer2.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.checkb_passwd_protect = wx.CheckBox( self, wx.ID_ANY, u"Enable Password Protection (Beta)", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.checkb_passwd_protect, 0, wx.ALL, 5 )

		paswd_settings_panel = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		paswd_settings_panel.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.input_display_username = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		paswd_settings_panel.Add( self.input_display_username, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		paswd_settings_panel.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.input_display_passwd = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD|wx.TE_READONLY )
		paswd_settings_panel.Add( self.input_display_passwd, 0, wx.ALL|wx.EXPAND, 5 )

		self.btn_modify_userinfo = wx.Button( self, wx.ID_ANY, u"Modify", wx.DefaultPosition, wx.DefaultSize, 0 )
		paswd_settings_panel.Add( self.btn_modify_userinfo, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		paswd_settings_panel.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer2.Add( paswd_settings_panel, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.init_page_data )
		self.checkb_passwd_protect.Bind( wx.EVT_CHECKBOX, self.change_panel_display_state )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def init_page_data( self, event ):
		event.Skip()

	def change_panel_display_state( self, event ):
		event.Skip()


