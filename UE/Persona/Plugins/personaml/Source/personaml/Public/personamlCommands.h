// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "CoreMinimal.h"
#include "Framework/Commands/Commands.h"
#include "personamlStyle.h"

class FpersonamlCommands : public TCommands<FpersonamlCommands>
{
public:

	FpersonamlCommands()
		: TCommands<FpersonamlCommands>(TEXT("personaml"), NSLOCTEXT("Contexts", "personaml", "personaml Plugin"), NAME_None, FpersonamlStyle::GetStyleSetName())
	{
	}

	// TCommands<> interface
	virtual void RegisterCommands() override;

public:
	TSharedPtr< FUICommandInfo > PluginAction;
};
