# Structure
To distinguish between different plugins they are divided based on organization.
The name of the organization is based on the manufacturer of the actual 
peripheral.
For instance all plugins of philips hue peripherals can be found in the
“Philips” organization. Within the organization every plugin is represented 
by a unique name. 

# Creating new plugins
When a new plugin is added it should inherent from the class `device`.
When it inherits this class it needs needs to implement various abstract 
methods.
This is needed to set basic information for devices such as name and type.
The peripheral specific behaviour of the plugin is defined in the setup method
and the linked activators.
Therefore every plugin requires and setup method.
These activators represent different actions a pheripheral can perform.
All activators linked to a plugin require a perform method to depict how state
changes should be handled.
All information that is required for the device to setup and maintain the 
connection with the peripheral is set in the required info. 

### Setup()
The setup method handles the initialization of the devices that is specific 
for the peripheral the plugin represents. 
For example the philips hue plugins all have require the id of the light in the
 hue bridge, this id is fetched during the setup function.

The setup function is called after the required info is set.
This allows the setup function to make use of the information contained in the 
required info and it can use the required info as a way of storing the 
information to be used in the perform method of the activators.

### Perform()
The perform methods translates the current state of an activator to an action 
that can be performed by the peripheral. 
For example, With the activators of philips hue devices this in when the REST
post is send to the bridge.




