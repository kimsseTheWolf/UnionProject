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
## Class import_category
###########################################################################

class import_category ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Import an Existing Category", pos = wx.DefaultPosition, size = wx.Size( 373,183 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Category Folder Location", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.input_folder_location = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer2.Add( self.input_folder_location, 0, wx.ALL|wx.EXPAND, 5 )

		self.btn_choose_location = wx.Button( self, wx.ID_ANY, u"Choose Folder Location", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.btn_choose_location, 0, wx.ALL|wx.EXPAND, 5 )

		btn_yesno = wx.StdDialogButtonSizer()
		self.btn_yesnoOK = wx.Button( self, wx.ID_OK )
		btn_yesno.AddButton( self.btn_yesnoOK )
		self.btn_yesnoCancel = wx.Button( self, wx.ID_CANCEL )
		btn_yesno.AddButton( self.btn_yesnoCancel )
		btn_yesno.Realize();

		bSizer2.Add( btn_yesno, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_choose_location.Bind( wx.EVT_BUTTON, self.choose_folder_location )
		self.btn_yesnoCancel.Bind( wx.EVT_BUTTON, self.close_window )
		self.btn_yesnoOK.Bind( wx.EVT_BUTTON, self.import_category )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def choose_folder_location( self, event ):
		event.Skip()

	def close_window( self, event ):
		event.Skip()

	def import_category( self, event ):
		event.Skip()


