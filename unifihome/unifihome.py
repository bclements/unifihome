import logging
from textual import events, log
from textual.app import App
from textual.widgets import Header, Footer, Placeholder, ScrollView

class UnifiHome(App):
    async def on_load(self, event: events.Load) -> None:                
        await self.bind("q", "quit", "Quit")
        await self.bind("escape", "quit", "Quit")

    async def on_mount(self, event: events.Mount) -> None:      
        body = ScrollView(gutter=1)

        await self.view.dock(Header(), edge="top")
        await self.view.dock(Footer(), edge="bottom")
        await self.view.dock(Placeholder(), edge="left", size=30, name="sidebar")
        await self.view.dock(Placeholder(), edge="right",name="main")

        # Dock the body in the remaining space
        #await self.view.dock(body, edge="right")

    
if __name__ == '__main__':
    print('Unifi Home is starting')
    UnifiHome.run(title='Unifi Home',log='textual.log')