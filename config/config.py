import os
from environments import Config, Development, Testing, Production

# Set environmental settings
# environment = 'testing'

environment_configuration = {
    'development': Development,
    'testing': Testing,
    'Production': Production
}
