import json
from copier_templates_extensions import ContextHook

class ExtraEnvExtension(ContextHook):
  def hook(self, context):
    extra_env = context.get('_extra_env', {})

    # Add the extra environment variables to self.environment
    if extra_env:
      print(extra_env)
      extra_env = json.loads(extra_env) if isinstance(extra_env, str) else extra_env
      print(extra_env)
      for key, value in extra_env.items():
        self.environment[key] = value
    
    return context