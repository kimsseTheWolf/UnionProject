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
## Class create_file_dialog
###########################################################################

class create_file_dialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Create a File...", pos = wx.DefaultPosition, size = wx.Size( 432,158 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"File name (With file extention)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer3.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.input_filename = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.input_filename, 0, wx.ALL|wx.EXPAND, 5 )

		btn_yesno = wx.StdDialogButtonSizer()
		self.btn_yesnoOK = wx.Button( self, wx.ID_OK )
		btn_yesno.AddButton( self.btn_yesnoOK )
		self.btn_yesnoCancel = wx.Button( self, wx.ID_CANCEL )
		btn_yesno.AddButton( self.btn_yesnoCancel )
		btn_yesno.Realize();

		bSizer3.Add( btn_yesno, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_yesnoCancel.Bind( wx.EVT_BUTTON, self.close_window )
		self.btn_yesnoOK.Bind( wx.EVT_BUTTON, self.create_file )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def close_window( self, event ):
		event.Skip()

	def create_file( self, event ):
		event.Skip()


