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
## Class import_file_dialog
###########################################################################

class import_file_dialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Import files...", pos = wx.DefaultPosition, size = wx.Size( 439,302 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Click the Import button to import, and click Apply to make progress", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.btn_import = wx.Button( self, wx.ID_ANY, u"Select Import Files", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.btn_import, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Selected files:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )

		m_listBox2Choices = []
		self.m_listBox2 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox2Choices, 0 )
		bSizer2.Add( self.m_listBox2, 1, wx.ALL|wx.EXPAND, 5 )

		btn_apply = wx.StdDialogButtonSizer()
		self.btn_applyApply = wx.Button( self, wx.ID_APPLY )
		btn_apply.AddButton( self.btn_applyApply )
		self.btn_applyCancel = wx.Button( self, wx.ID_CANCEL )
		btn_apply.AddButton( self.btn_applyCancel )
		btn_apply.Realize();

		bSizer2.Add( btn_apply, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_import.Bind( wx.EVT_BUTTON, self.choose_files )
		self.btn_applyApply.Bind( wx.EVT_BUTTON, self.import_files )
		self.btn_applyCancel.Bind( wx.EVT_BUTTON, self.close_window )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def choose_files( self, event ):
		event.Skip()

	def import_files( self, event ):
		event.Skip()

	def close_window( self, event ):
		event.Skip()


