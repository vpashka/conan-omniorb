#include <iostream>
#include <omniORB4/CORBA.h>

int main(int arc, char **argv) {
  CORBA::ORB_ptr orb = CORBA::ORB_init(arc,argv,"omniORB4");
}
