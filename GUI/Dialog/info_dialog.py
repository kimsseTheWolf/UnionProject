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
## Class InfoDialog
###########################################################################

class InfoDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Info", pos = wx.DefaultPosition, size = wx.Size( 322,179 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.content = wx.StaticText( self, wx.ID_ANY, u"Info Content", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.content.Wrap( -1 )

		bSizer5.Add( self.content, 1, wx.ALL|wx.EXPAND, 5 )

		btn_yn = wx.StdDialogButtonSizer()
		self.btn_ynOK = wx.Button( self, wx.ID_OK )
		btn_yn.AddButton( self.btn_ynOK )
		btn_yn.Realize();

		bSizer5.Add( btn_yn, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_ynOK.Bind( wx.EVT_BUTTON, self.exit )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def exit( self, event ):
		event.Skip()


