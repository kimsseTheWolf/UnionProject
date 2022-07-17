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
## Class CreateCategoryWindow
###########################################################################

class CreateCategoryWindow ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Create a new category..", pos = wx.DefaultPosition, size = wx.Size( 494,334 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Category Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.input_category_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.input_category_name, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Description for the Categoory (Selective)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer2.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.input_description = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer2.Add( self.input_description, 1, wx.ALL|wx.EXPAND, 5 )

		btn_ynSelect = wx.StdDialogButtonSizer()
		self.btn_ynSelectOK = wx.Button( self, wx.ID_OK )
		btn_ynSelect.AddButton( self.btn_ynSelectOK )
		self.btn_ynSelectCancel = wx.Button( self, wx.ID_CANCEL )
		btn_ynSelect.AddButton( self.btn_ynSelectCancel )
		btn_ynSelect.Realize();

		bSizer2.Add( btn_ynSelect, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_ynSelectCancel.Bind( wx.EVT_BUTTON, self.exit_window )
		self.btn_ynSelectOK.Bind( wx.EVT_BUTTON, self.create_new_category )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def exit_window( self, event ):
		event.Skip()

	def create_new_category( self, event ):
		event.Skip()


