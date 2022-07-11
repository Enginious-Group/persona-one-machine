// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "Modules/ModuleManager.h"
#include "DesktopPlatform/Public/IDesktopPlatform.h"
#include "DesktopPlatform/Public/DesktopPlatformModule.h"
#include "Engine/GameEngine.h"
#include "EngineGlobals.h"
#include "SlateCore.h"
#include "Runtime/Engine/Classes/Engine/GameViewportClient.h"
#include "Framework/Application/SlateApplication.h"
#include "Interfaces/IPluginManager.h"

class FToolBarBuilder;
class FMenuBuilder;

class FpersonamlModule : public IModuleInterface
{
public:

	/** IModuleInterface implementation */
	virtual void StartupModule() override;
	virtual void ShutdownModule() override;
	
	/** This function will be bound to Command. */
	static FReply LaunchOpenFileDialogue();
	void PluginButtonClicked();

	
private:

	void RegisterMenus();


private:
	TSharedPtr<class FUICommandList> PluginCommands;
};
