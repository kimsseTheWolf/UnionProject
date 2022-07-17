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
## Class export_category
###########################################################################

class export_category ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Export Category", pos = wx.DefaultPosition, size = wx.Size( 364,238 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Select a category you want to export", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

		btn_category_choices_listChoices = []
		self.btn_category_choices_list = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, btn_category_choices_listChoices, 0 )
		bSizer1.Add( self.btn_category_choices_list, 0, wx.ALL|wx.EXPAND, 5 )

		self.statictext2 = wx.StaticText( self, wx.ID_ANY, u"Select a location you want to save your export", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.statictext2.Wrap( -1 )

		bSizer1.Add( self.statictext2, 0, wx.ALL, 5 )

		self.input_export_dst_display = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer1.Add( self.input_export_dst_display, 0, wx.ALL|wx.EXPAND, 5 )

		self.btn_choose_file = wx.Button( self, wx.ID_ANY, u"Choose Location", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.btn_choose_file, 0, wx.ALL, 5 )

		btn_apply = wx.StdDialogButtonSizer()
		self.btn_applyApply = wx.Button( self, wx.ID_APPLY )
		btn_apply.AddButton( self.btn_applyApply )
		self.btn_applyCancel = wx.Button( self, wx.ID_CANCEL )
		btn_apply.AddButton( self.btn_applyCancel )
		btn_apply.Realize();

		bSizer1.Add( btn_apply, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.init_data )
		self.btn_choose_file.Bind( wx.EVT_BUTTON, self.open_file_picker )
		self.btn_applyApply.Bind( wx.EVT_BUTTON, self.export_category )
		self.btn_applyCancel.Bind( wx.EVT_BUTTON, self.close_window )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def init_data( self, event ):
		event.Skip()

	def open_file_picker( self, event ):
		event.Skip()

	def export_category( self, event ):
		event.Skip()

	def close_window( self, event ):
		event.Skip()


