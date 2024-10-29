from copier_templates_extensions import ContextHook

class ExtraEnvExtension(ContextHook):
  def hook(self, context):
    print("ExtraEnvExtension hook", context)
    extra_env = context.get('_extra_env', {})

    # Add the extra environment variables to self.environment
    if extra_env:
      for key, value in extra_env.items():
        self.environment[key] = value
    
    return context