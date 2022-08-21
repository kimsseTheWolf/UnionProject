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
## Class projectList
###########################################################################

class projectList ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Project List - Union Project", pos = wx.DefaultPosition, size = wx.Size( 624,506 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Information of this category:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Microsoft YaHei UI" ) )

		bSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.text_name = wx.StaticText( self, wx.ID_ANY, u"Name: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_name.Wrap( -1 )

		bSizer1.Add( self.text_name, 0, wx.ALL, 5 )

		self.text_create_date = wx.StaticText( self, wx.ID_ANY, u"Create Date: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_create_date.Wrap( -1 )

		bSizer1.Add( self.text_create_date, 0, wx.ALL, 5 )

		self.text_description = wx.StaticText( self, wx.ID_ANY, u"Description", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_description.Wrap( -1 )

		bSizer1.Add( self.text_description, 0, wx.ALL, 5 )

		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		self.btn_return_category_list = wx.Button( self, wx.ID_ANY, u"Return to Category List", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.btn_return_category_list, 0, wx.ALL|wx.EXPAND, 5 )

		self.btn_display_category_properties = wx.Button( self, wx.ID_ANY, u"Check Category Properties", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.btn_display_category_properties, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( gSizer2, 0, wx.EXPAND, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Ongoing Projects", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		self.m_staticText6.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Microsoft YaHei UI" ) )

		bSizer1.Add( self.m_staticText6, 0, wx.ALL, 5 )

		list_display_project_listChoices = []
		self.list_display_project_list = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, list_display_project_listChoices, wx.LB_HSCROLL )
		bSizer1.Add( self.list_display_project_list, 1, wx.ALL|wx.EXPAND, 5 )

		self.btn_checkFinished = wx.Button( self, wx.ID_ANY, u"Display Finished Project", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.btn_checkFinished, 0, wx.ALL|wx.EXPAND, 5 )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.btn_create_project = wx.Button( self, wx.ID_ANY, u"Create new Project", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.btn_create_project, 1, wx.ALL|wx.EXPAND, 5 )

		self.btn_delete_project = wx.Button( self, wx.ID_ANY, u"Delete selected Project", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.btn_delete_project, 1, wx.ALL|wx.EXPAND, 5 )

		self.btn_modify_project = wx.Button( self, wx.ID_ANY, u"Modify selected Project", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.btn_modify_project, 1, wx.ALL|wx.EXPAND, 5 )

		self.btn_refresh = wx.Button( self, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.btn_refresh, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( gSizer1, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.btn_menu = wx.MenuBar( 0 )
		self.btn_file = wx.Menu()
		self.btn_file_project_properties = wx.MenuItem( self.btn_file, wx.ID_ANY, u"Check Project Property", wx.EmptyString, wx.ITEM_NORMAL )
		self.btn_file.Append( self.btn_file_project_properties )

		self.btn_file_category_properties = wx.MenuItem( self.btn_file, wx.ID_ANY, u"Check Category Property", wx.EmptyString, wx.ITEM_NORMAL )
		self.btn_file.Append( self.btn_file_category_properties )

		self.btn_file_export = wx.MenuItem( self.btn_file, wx.ID_ANY, u"Export Selected Project", wx.EmptyString, wx.ITEM_NORMAL )
		self.btn_file.Append( self.btn_file_export )

		self.btn_file.AppendSeparator()

		self.btn_file_settings = wx.MenuItem( self.btn_file, wx.ID_ANY, u"Settings", wx.EmptyString, wx.ITEM_NORMAL )
		self.btn_file.Append( self.btn_file_settings )

		self.btn_file_about = wx.MenuItem( self.btn_file, wx.ID_ANY, u"About Union Project", wx.EmptyString, wx.ITEM_NORMAL )
		self.btn_file.Append( self.btn_file_about )

		self.btn_menu.Append( self.btn_file, u"File" )

		self.SetMenuBar( self.btn_menu )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_ACTIVATE, self.init_data )
		self.btn_return_category_list.Bind( wx.EVT_BUTTON, self.return_category_list )
		self.btn_display_category_properties.Bind( wx.EVT_BUTTON, self.check_category_properties )
		self.list_display_project_list.Bind( wx.EVT_LISTBOX_DCLICK, self.enter_file_list )
		self.btn_checkFinished.Bind( wx.EVT_BUTTON, self.open_finished_list )
		self.btn_create_project.Bind( wx.EVT_BUTTON, self.create_project )
		self.btn_delete_project.Bind( wx.EVT_BUTTON, self.delete_project )
		self.btn_modify_project.Bind( wx.EVT_BUTTON, self.modify_project )
		self.btn_refresh.Bind( wx.EVT_BUTTON, self.refresh_list )
		self.Bind( wx.EVT_MENU, self.display_project_property, id = self.btn_file_project_properties.GetId() )
		self.Bind( wx.EVT_MENU, self.check_category_properties, id = self.btn_file_category_properties.GetId() )
		self.Bind( wx.EVT_MENU, self.export_file, id = self.btn_file_export.GetId() )
		self.Bind( wx.EVT_MENU, self.open_settings, id = self.btn_file_settings.GetId() )
		self.Bind( wx.EVT_MENU, self.open_about, id = self.btn_file_about.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def init_data( self, event ):
		event.Skip()

	def return_category_list( self, event ):
		event.Skip()

	def check_category_properties( self, event ):
		event.Skip()

	def enter_file_list( self, event ):
		event.Skip()

	def open_finished_list( self, event ):
		event.Skip()

	def create_project( self, event ):
		event.Skip()

	def delete_project( self, event ):
		event.Skip()

	def modify_project( self, event ):
		event.Skip()

	def refresh_list( self, event ):
		event.Skip()

	def display_project_property( self, event ):
		event.Skip()


	def export_file( self, event ):
		event.Skip()

	def open_settings( self, event ):
		event.Skip()

	def open_about( self, event ):
		event.Skip()


