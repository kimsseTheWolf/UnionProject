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
## Class finishedPeoject
###########################################################################

class finishedPeoject ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Finished Project", pos = wx.DefaultPosition, size = wx.Size( 654,419 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Finished Project", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		self.m_staticText10.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Microsoft YaHei UI" ) )

		bSizer4.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"NOTE: All the project displayed here are all finished!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		self.m_staticText11.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_staticText11.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )

		bSizer4.Add( self.m_staticText11, 0, wx.ALL, 5 )

		list_display_project_listChoices = []
		self.list_display_project_list = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, list_display_project_listChoices, 0 )
		bSizer4.Add( self.list_display_project_list, 1, wx.ALL|wx.EXPAND, 5 )

		self.btn_refresh = wx.Button( self, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.btn_refresh, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

		self.btn_delete_project = wx.Button( self, wx.ID_ANY, u"Delete selected Project", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.btn_delete_project, 0, wx.ALL|wx.EXPAND, 5 )

		self.btn_modify_project = wx.Button( self, wx.ID_ANY, u"Modify selected project", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.btn_modify_project, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer4.Add( gSizer3, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.list_display_project_list.Bind( wx.EVT_LISTBOX_DCLICK, self.enter_file_list )
		self.btn_refresh.Bind( wx.EVT_BUTTON, self.refresh_list )
		self.btn_delete_project.Bind( wx.EVT_BUTTON, self.delete_project )
		self.btn_modify_project.Bind( wx.EVT_BUTTON, self.modify_project )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def enter_file_list( self, event ):
		event.Skip()

	def refresh_list( self, event ):
		event.Skip()

	def delete_project( self, event ):
		event.Skip()

	def modify_project( self, event ):
		event.Skip()


