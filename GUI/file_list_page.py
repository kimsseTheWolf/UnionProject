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
## Class file_list
###########################################################################

class file_list ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"File List - Union Project", pos = wx.DefaultPosition, size = wx.Size( 604,440 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"File List", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Microsoft YaHei UI" ) )

		bSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )

		list_fileListChoices = []
		self.list_fileList = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, list_fileListChoices, 0 )
		bSizer1.Add( self.list_fileList, 1, wx.ALL|wx.EXPAND, 5 )

		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		self.btn_open = wx.Button( self, wx.ID_ANY, u"Open selected file", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.btn_open, 0, wx.ALL|wx.EXPAND, 5 )

		self.btn_delete = wx.Button( self, wx.ID_ANY, u"Delete selected file", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.btn_delete, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( gSizer2, 0, wx.EXPAND, 5 )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

		self.btn_create_file = wx.Button( self, wx.ID_ANY, u"Create a new file", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.btn_create_file, 0, wx.ALL|wx.EXPAND, 5 )

		self.btn_import = wx.Button( self, wx.ID_ANY, u"Import file(s) from local", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.btn_import, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( gSizer3, 0, wx.EXPAND, 5 )

		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

		self.btn_refresh = wx.Button( self, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.btn_refresh, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.btn_file = wx.Menu()
		self.btn_file_create = wx.MenuItem( self.btn_file, wx.ID_ANY, u"Create a new file", wx.EmptyString, wx.ITEM_NORMAL )
		self.btn_file.Append( self.btn_file_create )

		self.btn_file_import = wx.MenuItem( self.btn_file, wx.ID_ANY, u"Import file(s) from local", wx.EmptyString, wx.ITEM_NORMAL )
		self.btn_file.Append( self.btn_file_import )

		self.btn_file_openLocation = wx.MenuItem( self.btn_file, wx.ID_ANY, u"Open selected file location...", wx.EmptyString, wx.ITEM_NORMAL )
		self.btn_file.Append( self.btn_file_openLocation )

		self.m_menubar1.Append( self.btn_file, u"File" )

		self.btn_properties = wx.Menu()
		self.btn_properties_categoryProp = wx.MenuItem( self.btn_properties, wx.ID_ANY, u"Check category properties", wx.EmptyString, wx.ITEM_NORMAL )
		self.btn_properties.Append( self.btn_properties_categoryProp )

		self.btn_properties_projectProp = wx.MenuItem( self.btn_properties, wx.ID_ANY, u"Check project properties", wx.EmptyString, wx.ITEM_NORMAL )
		self.btn_properties.Append( self.btn_properties_projectProp )

		self.btn_properties_fileProp = wx.MenuItem( self.btn_properties, wx.ID_ANY, u"Check selected file properties", wx.EmptyString, wx.ITEM_NORMAL )
		self.btn_properties.Append( self.btn_properties_fileProp )

		self.m_menubar1.Append( self.btn_properties, u"Properties" )

		self.btn_more = wx.Menu()
		self.btn_more_about = wx.MenuItem( self.btn_more, wx.ID_ANY, u"About Union Project", wx.EmptyString, wx.ITEM_NORMAL )
		self.btn_more.Append( self.btn_more_about )

		self.btn_more_settings = wx.MenuItem( self.btn_more, wx.ID_ANY, u"Settings", wx.EmptyString, wx.ITEM_NORMAL )
		self.btn_more.Append( self.btn_more_settings )

		self.m_menubar1.Append( self.btn_more, u"More" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_ACTIVATE, self.init_data )
		self.list_fileList.Bind( wx.EVT_LISTBOX_DCLICK, self.open_file )
		self.btn_open.Bind( wx.EVT_BUTTON, self.open_file )
		self.btn_delete.Bind( wx.EVT_BUTTON, self.delete_file )
		self.btn_create_file.Bind( wx.EVT_BUTTON, self.create_file )
		self.btn_import.Bind( wx.EVT_BUTTON, self.import_file )
		self.btn_refresh.Bind( wx.EVT_BUTTON, self.refresh )
		self.Bind( wx.EVT_MENU, self.create_file, id = self.btn_file_create.GetId() )
		self.Bind( wx.EVT_MENU, self.import_file, id = self.btn_file_import.GetId() )
		self.Bind( wx.EVT_MENU, self.openFileLocation, id = self.btn_file_openLocation.GetId() )
		self.Bind( wx.EVT_MENU, self.display_category_properties, id = self.btn_properties_categoryProp.GetId() )
		self.Bind( wx.EVT_MENU, self.display_project_properties, id = self.btn_properties_projectProp.GetId() )
		self.Bind( wx.EVT_MENU, self.display_file_properties, id = self.btn_properties_fileProp.GetId() )
		self.Bind( wx.EVT_MENU, self.display_about, id = self.btn_more_about.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def init_data( self, event ):
		event.Skip()

	def open_file( self, event ):
		event.Skip()


	def delete_file( self, event ):
		event.Skip()

	def create_file( self, event ):
		event.Skip()

	def import_file( self, event ):
		event.Skip()

	def refresh( self, event ):
		event.Skip()



	def openFileLocation( self, event ):
		event.Skip()

	def display_category_properties( self, event ):
		event.Skip()

	def display_project_properties( self, event ):
		event.Skip()

	def display_file_properties( self, event ):
		event.Skip()

	def display_about( self, event ):
		event.Skip()


