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
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Union Project", pos = wx.DefaultPosition, size = wx.Size( 597,361 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Category List", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Microsoft YaHei UI" ) )

		bSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Select a category to go on", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )

		category_listChoices = []
		self.category_list = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, category_listChoices, wx.LB_HSCROLL )
		bSizer1.Add( self.category_list, 1, wx.ALL|wx.EXPAND, 5 )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.btn_create_category = wx.Button( self, wx.ID_ANY, u"Create new Category", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.btn_create_category, 0, wx.ALL|wx.EXPAND, 5 )

		self.btn_delete_category = wx.Button( self, wx.ID_ANY, u"Delete Selected Category", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.btn_delete_category, 0, wx.ALL|wx.EXPAND, 5 )

		self.btn_modify = wx.Button( self, wx.ID_ANY, u"Modify Selected Category", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.btn_modify, 1, wx.ALL|wx.EXPAND, 5 )

		self.btn_refresh = wx.Button( self, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.btn_refresh, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( gSizer1, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.btn_menu = wx.MenuBar( 0 )
		self.menu_file = wx.Menu()
		self.menu_file_properties = wx.MenuItem( self.menu_file, wx.ID_ANY, u"Check Category Properties", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.Append( self.menu_file_properties )

		self.menu_file.AppendSeparator()

		self.menu_file_export = wx.MenuItem( self.menu_file, wx.ID_ANY, u"Export And Backup", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.Append( self.menu_file_export )

		self.menu_file_import = wx.MenuItem( self.menu_file, wx.ID_ANY, u"Import Existing Projects", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.Append( self.menu_file_import )

		self.menu_file.AppendSeparator()

		self.menu_file_settings = wx.MenuItem( self.menu_file, wx.ID_ANY, u"Settings", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.Append( self.menu_file_settings )

		self.menu_file_about = wx.MenuItem( self.menu_file, wx.ID_ANY, u"About Union Project", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.Append( self.menu_file_about )

		self.btn_menu.Append( self.menu_file, u"File" )

		self.SetMenuBar( self.btn_menu )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_ACTIVATE, self.refresh_category_list )
		self.Bind( wx.EVT_ACTIVATE_APP, self.refresh_category_list )
		self.Bind( wx.EVT_CLOSE, self.clearData )
		self.Bind( wx.EVT_HIBERNATE, self.refresh_category_list )
		self.category_list.Bind( wx.EVT_LISTBOX, self.sync_category_name )
		self.category_list.Bind( wx.EVT_LISTBOX_DCLICK, self.enter_category )
		self.btn_create_category.Bind( wx.EVT_BUTTON, self.create_category )
		self.btn_delete_category.Bind( wx.EVT_BUTTON, self.delete_category )
		self.btn_modify.Bind( wx.EVT_BUTTON, self.modify_category )
		self.btn_refresh.Bind( wx.EVT_BUTTON, self.refresh_category_list )
		self.Bind( wx.EVT_MENU, self.display_properties, id = self.menu_file_properties.GetId() )
		self.Bind( wx.EVT_MENU, self.export_category, id = self.menu_file_export.GetId() )
		self.Bind( wx.EVT_MENU, self.import_category, id = self.menu_file_import.GetId() )
		self.Bind( wx.EVT_MENU, self.open_settings, id = self.menu_file_settings.GetId() )
		self.Bind( wx.EVT_MENU, self.open_about, id = self.menu_file_about.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def refresh_category_list( self, event ):
		event.Skip()


	def clearData( self, event ):
		event.Skip()


	def sync_category_name( self, event ):
		event.Skip()

	def enter_category( self, event ):
		event.Skip()

	def create_category( self, event ):
		event.Skip()

	def delete_category( self, event ):
		event.Skip()

	def modify_category( self, event ):
		event.Skip()


	def display_properties( self, event ):
		event.Skip()

	def export_category( self, event ):
		event.Skip()

	def import_category( self, event ):
		event.Skip()

	def open_settings( self, event ):
		event.Skip()

	def open_about( self, event ):
		event.Skip()


