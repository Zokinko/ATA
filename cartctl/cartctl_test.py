#!/usr/bin/env python3
"""
Example of usage/test of Cart controller implementation.
"""

import sys
from cartctl import CartCtl
from cart import Cart, CargoReq
from jarvisenv import Jarvis
import unittest

def log(msg):
    "simple logging"
    print('  %s' % msg)

class TestCartRequests(unittest.TestCase):

    def test_happy(self):
        "Happy-path test"

        def add_load(c: CartCtl, cargo_req: CargoReq):
            "callback for schedulled load"
            log('%d: Requesting %s at %s' % \
                (Jarvis.time(), cargo_req, cargo_req.src))
            c.request(cargo_req)

        def on_move(c: Cart):
            "example callback (for assert)"
            # put some asserts here
            log('%d: Cart is moving %s->%s' % (Jarvis.time(), c.pos, c.data))

        def on_load(c: Cart, cargo_req: CargoReq):
            "example callback for logging"
            log('%d: Cart at %s: loading: %s' % (Jarvis.time(), c.pos, cargo_req))
            log(c)
            cargo_req.context = "loaded"

        def on_unload(c: Cart, cargo_req: CargoReq):
            "example callback (for assert)"
            # put some asserts here
            log('%d: Cart at %s: unloading: %s' % (Jarvis.time(), c.pos, cargo_req))
            log(c)
            self.assertEqual('loaded', cargo_req.context)
            cargo_req.context = 'unloaded'
            # if cargo_req.content == 'helmet':
            #     self.assertEqual('B', c.pos)
            # if cargo_req.content == 'heart':
            #     self.assertEqual('A', c.pos)
            # #if cargo_req.content.startswith('bracelet'):
            # #    self.assertEqual('C', c.pos)
            # if cargo_req.content == 'braceletR':
            #     self.assertEqual('A', c.pos)
            # if cargo_req.content == 'braceletL':
            #     self.assertEqual('C', c.pos)

        
        def test_1_heavy_material(self):
            # Setup Cart
            # 4 slots, 150 kg max payload capacity, 2=max debug
            cart_dev = Cart(4, 150, 0)
            cart_dev.onmove = on_move

            # Setup Cart Controller
            c = CartCtl(cart_dev, Jarvis)

            # Setup Cargo to move
            helmet = CargoReq('A', 'B', 160, 'helmet')
            helmet.onload = on_load
            helmet.onunload = on_unload

            # Setup Plan
            Jarvis.reset_scheduler()
            #         when  event     called_with_params
            Jarvis.plan(10, add_load, (c,helmet))
            
            # Exercise + Verify indirect output
            Jarvis.run()

            # Verify direct output
            log(cart_dev)
            self.assertNotEqual('A',cart_dev.pos)

        def test_case_1(self):
            #slots, max payload capacity, 2=max debug
            cart_dev = Cart(1, 150, 0)
            cart_dev.onmove = on_move

            # Setup Cart Controller
            c = CartCtl(cart_dev, Jarvis)

            # Setup Cargo to move
            helmet = CargoReq('A', 'B', 30, 'helmet')
            helmet.onload = on_load
            helmet.onunload = on_unload


            # Setup Plan
            Jarvis.reset_scheduler()
            #         when  event     called_with_params
            Jarvis.plan(10, add_load, (c,helmet))

            Jarvis.run()

            # Verify direct output
            log(cart_dev)
            self.assertTrue(cart_dev.empty())
            self.assertEqual('unloaded', helmet.context)
            self.assertEqual(cart_dev.pos, 'B')

        def test_case_5(self):
            #slots, max payload capacity, 2=max debug
            cart_dev = Cart(3, 150, 0)
            cart_dev.onmove = on_move

            # Setup Cart Controller
            c = CartCtl(cart_dev, Jarvis)

            # Setup Cargo to move
            helmet = CargoReq('B', 'D', 10, 'helmet')
            helmet.onload = on_load
            helmet.onunload = on_unload
            # Setup Cargo to move
            heart = CargoReq('B', 'D', 15, 'heart')
            heart.onload = on_load
            heart.onunload = on_unload


            # Setup Plan
            Jarvis.reset_scheduler()
            #         when  event     called_with_params
            Jarvis.plan(10, add_load, (c,helmet))
            Jarvis.plan(15, add_load, (c,heart))

            Jarvis.run()

            # Verify direct output
            log(cart_dev)
            self.assertTrue(cart_dev.empty())
            self.assertEqual('unloaded', helmet.context)
            self.assertEqual('unloaded', heart.context)
            self.assertEqual(cart_dev.pos, 'D')

        def test_case_18(self):
            #slots, max payload capacity, 2=max debug
            cart_dev = Cart(4, 50, 0)
            cart_dev.onmove = on_move

            # Setup Cart Controller
            c = CartCtl(cart_dev, Jarvis)

            # Setup Cargo to move
            helmet = CargoReq('B', 'A', 10, 'helmet')
            helmet.onload = on_load
            helmet.onunload = on_unload

            heart = CargoReq('B', 'A', 15, 'heart')
            heart.onload = on_load
            heart.onunload = on_unload

            braceletR = CargoReq('B', 'A', 5, 'braceletR')
            braceletR.onload = on_load
            braceletR.onunload = on_unload


            # Setup Plan
            Jarvis.reset_scheduler()
            #         when  event     called_with_params
            Jarvis.plan(5, add_load, (c,helmet))
            Jarvis.plan(15, add_load, (c,heart))
            Jarvis.plan(45, add_load, (c,braceletR))

            Jarvis.run()

            # Verify direct output
            log(cart_dev)
            self.assertTrue(cart_dev.empty())
            self.assertEqual('unloaded', helmet.context)
            self.assertEqual('unloaded', heart.context)
            self.assertEqual('unloaded', braceletR.context)
            self.assertEqual(cart_dev.pos, 'A')
            self.assertLess(c.time(), 120)
            self.assertGreater(c.time(), 60)
        
        def test_case_21(self):
            #slots, max payload capacity, 2=max debug
            cart_dev = Cart(1, 500, 0)
            cart_dev.onmove = on_move

            # Setup Cart Controller
            c = CartCtl(cart_dev, Jarvis)

            # Setup Cargo to move
            helmet = CargoReq('B', 'A', 230, 'helmet')
            helmet.onload = on_load
            helmet.onunload = on_unload


            # Setup Plan
            Jarvis.reset_scheduler()
            #         when  event     called_with_params
            Jarvis.plan(10, add_load, (c,helmet))

            Jarvis.run()

            # Verify direct output
            log(cart_dev)
            self.assertTrue(cart_dev.empty())
            self.assertEqual('unloaded', helmet.context)
            self.assertEqual(cart_dev.pos, 'A')

        def test_case_10(self):
            #slots, max payload capacity, 2=max debug
            cart_dev = Cart(3, 50, 0)
            cart_dev.onmove = on_move

            # Setup Cart Controller
            c = CartCtl(cart_dev, Jarvis)

            # Setup Cargo to move
            helmet = CargoReq('D', 'A', 40, 'helmet')
            helmet.onload = on_load
            helmet.onunload = on_unload


            # Setup Plan
            Jarvis.reset_scheduler()
            #         when  event     called_with_params
            Jarvis.plan(10, add_load, (c,helmet))

            Jarvis.run()

            # Verify direct output
            log(cart_dev)
            self.assertTrue(cart_dev.empty())
            self.assertEqual('unloaded', helmet.context)
            self.assertEqual(cart_dev.pos, 'A')

        #test_1_heavy_material(self)
        print("test_case_1========================================================================")
        test_case_1(self)
        print("test_case_5========================================================================")
        test_case_5(self)
        print("test_case_18========================================================================")
        test_case_18(self)
        print("test_case_21========================================================================")
        test_case_21(self)
        print("test_case_10========================================================================")
        test_case_10(self)

if __name__ == "__main__":
    unittest.main()