# Structure
To distinguish between different plugins they are divided based on collection.
The name of the collection is based on the manufacturer of the actual 
peripheral.
For instance all plugins of philips hue peripherals can be found in the
“Philips” collection. Within the collection every plugin is represented 
by a unique name. 

# Creating new plugins
Creating new plugins consists of implementing two classes, `Device` and `Activator`,
 and adding information about these classes into the `deviceConfig`.

When a new plugin is added it should inherit from the class `Device`.
When it inherits this class, it needs to implement the setup method.

Furthermore, activators represent different actions a peripheral can perform.
All activators should inherit from the class `Activator`.
All activators require a perform method to depict how state
changes should be handled.

All static information that is needed for both the `Device` and `Activator`
class should be added to the `deviceConfig`.
This includes for example, name, module and default state.

### Setup()
The setup method handles the initialization of the devices that is specific 
for the peripheral the plugin represents. 
For example the philips hue plugins all require the id of the light in the
 hue bridge, this id is fetched during the setup function.

### Perform()
The perform methods translate the current state of an activator to an action 
that can be performed by the peripheral. 
For example, with the activators of philips hue devices this in when the REST
post is send to the bridge.

### deviceConfig
The `deviceConfig` file contains all the static information needed in the plugin.
As it is rather self-explanatory we have added a example below.
Every collection has its own entry into the file.
In the example the only collection is "Mock", it has one plugin called "Lock".
The following fields are mandatory for each implementation of the `Device` class: "module", "class", "type".
For both `Device` and`Activator` all fields shown below are mandatory.
It is not required to have any information in the "required_info" but the field has to be there.

```json
{
"Mock": {
    "Lock": {
      "module": "plugins.mock.lock.Lock",
      "class": "Lock",
      "type": "Lock",
      "required_info": {
        "bridge_ip": "127.0.0.1",
        "bridge_port": "80"
      },
      "activators": [
        {
          "module": "plugins.mock.lock.ActivateLock",
          "rank": 0,
          "class": "ActivateLock",
          "name": "Activate",
          "type": "bool",
          "state": true
        }
      ]
    }
  }
}
```

# Examples
To have a look at some really simple implementations take a look at the plugins
of the mock collection.
These should be easily understood and give an idea about what a plugin should 
look like.
For more real life and working examples take a look at the plugins of the 
"Philips" collection.
These are the plugins used for installing new devices for the peripherals of 
the Philips hue.