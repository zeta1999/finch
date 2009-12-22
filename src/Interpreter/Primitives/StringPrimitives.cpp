#include <iostream>

#include "StringPrimitives.h"
#include "DynamicObject.h"
#include "Environment.h"
#include "Object.h"

namespace Finch
{
    Ref<Object> StringAdd(Ref<Object> thisRef, Environment & env,
                           String message, const vector<Ref<Object> > & args)
    {
        // dynamically convert the object to a string
        vector<Ref<Object> > noArgs;
        Ref<Object> toString = args[0]->Receive(args[0], env, "to-string", noArgs);
        
        return Object::NewString(env, thisRef->AsString() + toString->AsString());
    }
    
    Ref<Object> StringLength(Ref<Object> thisRef, Environment & env,
                          String message, const vector<Ref<Object> > & args)
    {
        return Object::NewNumber(env, thisRef->AsString().size());
    }
    
    Ref<Object> StringAt(Ref<Object> thisRef, Environment & env,
                          String message, const vector<Ref<Object> > & args)
    {
        String thisString = thisRef->AsString();
        int    index      = static_cast<int>(args[0]->AsNumber());
        
        if ((index >= 0) && (index < thisString.size()))
        {
            String substring;
            substring.push_back(thisString[index]);
            return Object::NewString(env, substring);
        }
        
        // out of bounds
        return env.Nil();
    }
}
