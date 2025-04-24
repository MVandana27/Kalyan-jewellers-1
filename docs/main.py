def define_env(env):
    """Define variables and macros for MkDocs"""
    
    # Add variables
    env.variables['company'] = "Kalyan Jewellers"
    env.variables['founded'] = 1993
    env.variables['showrooms'] = 150
    
    # Create a macro
    @env.macro
    def jewelry_type(type, description):
        return f"""
<div class='jewelry-card'>
<h3>{type} Collection</h3>
<p>{description}</p>
</div>
        """