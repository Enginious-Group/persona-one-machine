// Copyright Epic Games, Inc. All Rights Reserved.

#include "personamlCommands.h"

#define LOCTEXT_NAMESPACE "FpersonamlModule"

void FpersonamlCommands::RegisterCommands()
{
	UI_COMMAND(PluginAction, "Persona", "Choose the concept file", EUserInterfaceActionType::Button, FInputGesture());
}

#undef LOCTEXT_NAMESPACE
