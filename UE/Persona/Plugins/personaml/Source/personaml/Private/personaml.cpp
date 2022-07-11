// Copyright Epic Games, Inc. All Rights Reserved.

#include "personaml.h"
#include "personamlStyle.h"
#include "personamlCommands.h"
#include "Misc/MessageDialog.h"
#include "ToolMenus.h"
#include "Interfaces/IPluginManager.h"

static const FName personamlTabName("personaml");

#define LOCTEXT_NAMESPACE "FpersonamlModule"

void FpersonamlModule::StartupModule()
{
	// This code will execute after your module is loaded into memory; the exact timing is specified in the .uplugin file per-module
	
	FpersonamlStyle::Initialize();
	FpersonamlStyle::ReloadTextures();

	FpersonamlCommands::Register();
	
	PluginCommands = MakeShareable(new FUICommandList);

	PluginCommands->MapAction(
		FpersonamlCommands::Get().PluginAction,
		FExecuteAction::CreateRaw(this, &FpersonamlModule::PluginButtonClicked),
		FCanExecuteAction());

	UToolMenus::RegisterStartupCallback(FSimpleMulticastDelegate::FDelegate::CreateRaw(this, &FpersonamlModule::RegisterMenus));
}

void FpersonamlModule::ShutdownModule()
{
	// This function may be called during shutdown to clean up your module.  For modules that support dynamic reloading,
	// we call this function before unloading the module.

	UToolMenus::UnRegisterStartupCallback(this);

	UToolMenus::UnregisterOwner(this);

	FpersonamlStyle::Shutdown();

	FpersonamlCommands::Unregister();
}

FReply FpersonamlModule::LaunchOpenFileDialogue()
{
	FString PluginDir = IPluginManager::Get().FindPlugin("personaml")->GetBaseDir();

	FString commandPath = FString(TEXT("py ")) + PluginDir + FString(TEXT("/Source/python/main.py -p ")) + PluginDir;

	const TCHAR* commandTchar = *commandPath;
	GEngine->Exec(NULL, commandTchar);
	return FReply::Handled();
}

void FpersonamlModule::PluginButtonClicked()
{
	LaunchOpenFileDialogue();
}

void FpersonamlModule::RegisterMenus()
{
	// Owner will be used for cleanup in call to UToolMenus::UnregisterOwner
	FToolMenuOwnerScoped OwnerScoped(this);

	{
		UToolMenu* Menu = UToolMenus::Get()->ExtendMenu("LevelEditor.MainMenu.Window");
		{
			FToolMenuSection& Section = Menu->FindOrAddSection("WindowLayout");
			Section.AddMenuEntryWithCommandList(FpersonamlCommands::Get().PluginAction, PluginCommands);
		}
	}

	{
		UToolMenu* ToolbarMenu = UToolMenus::Get()->ExtendMenu("LevelEditor.LevelEditorToolBar");
		{
			FToolMenuSection& Section = ToolbarMenu->FindOrAddSection("Settings");
			{
				FToolMenuEntry& Entry = Section.AddEntry(FToolMenuEntry::InitToolBarButton(FpersonamlCommands::Get().PluginAction));
				Entry.SetCommandList(PluginCommands);
			}
		}
	}
}

#undef LOCTEXT_NAMESPACE
	
IMPLEMENT_MODULE(FpersonamlModule, personaml)